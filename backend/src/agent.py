import logging
from dataclasses import dataclass, field
from typing import Annotated

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    WorkerOptions,
    cli,
    metrics,
    tokenize,
    function_tool,
    RunContext
)
from livekit.plugins import murf, silero, google, deepgram, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

logger = logging.getLogger("agent")

load_dotenv(".env.local")


# Coffee Shop Menu
MENU = {
    "coffee": {
        "Espresso": {"S": 2.50, "M": 3.00, "L": 3.50},
        "Americano": {"S": 3.00, "M": 3.50, "L": 4.00},
        "Latte": {"S": 3.50, "M": 4.00, "L": 4.50},
        "Cappuccino": {"S": 3.50, "M": 4.00, "L": 4.50},
        "Mocha": {"S": 4.00, "M": 4.50, "L": 5.00},
        "Flat White": {"S": 3.75, "M": 4.25, "L": 4.75},
        "Macchiato": {"S": 3.25, "M": 3.75, "L": 4.25},
    },
    "tea": {
        "Green Tea": {"S": 2.50, "M": 3.00, "L": 3.50},
        "Black Tea": {"S": 2.50, "M": 3.00, "L": 3.50},
        "Chai Latte": {"S": 3.50, "M": 4.00, "L": 4.50},
        "Herbal Tea": {"S": 2.75, "M": 3.25, "L": 3.75},
    },
    "pastries": {
        "Croissant": 3.50,
        "Chocolate Muffin": 3.75,
        "Blueberry Muffin": 3.75,
        "Cinnamon Roll": 4.25,
        "Banana Bread": 3.50,
        "Cookie": 2.50,
    },
    "extras": {
        "Extra Shot": 0.75,
        "Almond Milk": 0.50,
        "Oat Milk": 0.50,
        "Soy Milk": 0.50,
        "Whipped Cream": 0.50,
        "Vanilla Syrup": 0.50,
        "Caramel Syrup": 0.50,
        "Hazelnut Syrup": 0.50,
    },
}


@dataclass
class OrderItem:
    """Represents a single item in the order"""
    category: str
    name: str
    size: str = "M"  # Default to Medium
    quantity: int = 1
    extras: list[str] = field(default_factory=list)
    price: float = 0.0

    def calculate_price(self) -> float:
        """Calculate the total price for this item"""
        base_price = 0.0
        
        if self.category in ["coffee", "tea"]:
            base_price = MENU[self.category][self.name][self.size]
        else:
            base_price = MENU[self.category][self.name]
        
        # Add extras
        extras_price = sum(MENU["extras"].get(extra, 0.0) for extra in self.extras)
        
        self.price = (base_price + extras_price) * self.quantity
        return self.price


@dataclass
class CustomerOrder:
    """Represents the complete customer order"""
    items: list[OrderItem] = field(default_factory=list)
    customer_name: str = ""
    
    def add_item(self, item: OrderItem):
        """Add an item to the order"""
        item.calculate_price()
        self.items.append(item)
    
    def get_total(self) -> float:
        """Calculate total order price"""
        return sum(item.price for item in self.items)
    
    def get_summary(self) -> str:
        """Get a formatted summary of the order"""
        if not self.items:
            return "No items in order yet."
        
        summary = []
        for idx, item in enumerate(self.items, 1):
            extras_str = f" with {', '.join(item.extras)}" if item.extras else ""
            size_str = f" ({item.size})" if item.category in ["coffee", "tea"] else ""
            summary.append(
                f"{idx}. {item.quantity}x {item.name}{size_str}{extras_str} - ${item.price:.2f}"
            )
        summary.append(f"\nTotal: ${self.get_total():.2f}")
        return "\n".join(summary)


class CoffeeBarista(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are Bella, a friendly and efficient coffee shop barista at 'Brew Haven Café'.
            
            Your personality:
            - Warm, welcoming, and enthusiastic about coffee
            - You make customers feel valued and help them discover their perfect drink
            - You're knowledgeable about different coffee types, brewing methods, and flavor profiles
            - You keep responses conversational and concise for voice interaction
            - You NEVER use emojis, asterisks, or complex formatting in your responses
            
            Your workflow:
            1. Greet customers warmly and ask how you can help them today
            2. When they're ready to order, use the get_menu tool to show available items
            3. Help them choose by describing drinks and making recommendations
            4. Use add_item_to_order to add each item they want
            5. Ask about size (Small, Medium, Large) for drinks
            6. Suggest extras like milk alternatives, syrups, or extra shots
            7. After each item, ask if they'd like anything else
            8. Use get_order_summary to review their complete order
            9. Ask for their name for the order using set_customer_name
            10. Confirm the total and finalize the order with finalize_order
            
            Important guidelines:
            - Always be proactive in using tools to manage the order
            - When customer mentions a drink, immediately add it using the tool
            - Suggest complementary items like pastries
            - Be helpful with dietary restrictions (we have almond, oat, and soy milk)
            - Keep the conversation flowing naturally like a real barista would
            - If they ask about the menu, use get_menu to show categories
            """,
        )
        self.current_order = CustomerOrder()

    @function_tool
    async def get_menu(self, context: RunContext, category: Annotated[str, "Category to show: 'all', 'coffee', 'tea', 'pastries', or 'extras'"] = "all") -> str:
        """Get the coffee shop menu. Use this when customer asks about available items or wants to see options.
        
        Args:
            category: Which category to display - 'all', 'coffee', 'tea', 'pastries', or 'extras'
        
        Returns:
            Formatted menu string
        """
        logger.info(f"Showing menu category: {category}")
        
        menu_text = []
        
        def format_category(cat_name: str, items: dict):
            lines = [f"\n{cat_name.upper()}:"]
            for item_name, price in items.items():
                if isinstance(price, dict):  # Coffee/Tea with sizes
                    prices = ", ".join([f"{size}: ${p:.2f}" for size, p in price.items()])
                    lines.append(f"  - {item_name} ({prices})")
                else:  # Pastries/Extras with single price
                    lines.append(f"  - {item_name}: ${price:.2f}")
            return lines
        
        if category == "all":
            for cat in ["coffee", "tea", "pastries", "extras"]:
                menu_text.extend(format_category(cat, MENU[cat]))
        elif category in MENU:
            menu_text.extend(format_category(category, MENU[category]))
        else:
            return f"Category '{category}' not found. Available categories: coffee, tea, pastries, extras, or all."
        
        return "\n".join(menu_text)

    @function_tool
    async def add_item_to_order(
        self,
        context: RunContext,
        category: Annotated[str, "Item category: 'coffee', 'tea', or 'pastries'"],
        name: Annotated[str, "Exact item name from the menu"],
        size: Annotated[str, "Size: 'S', 'M', or 'L' (only for coffee and tea)"] = "M",
        quantity: Annotated[int, "Quantity"] = 1,
        extras: Annotated[list[str], "List of extras to add"] = None,
    ) -> str:
        """Add an item to the customer's order. Use this whenever they mention wanting a drink or food item.
        
        Args:
            category: The category of the item
            name: Exact name of the item from the menu
            size: Size selection (S/M/L) - only for coffee and tea
            quantity: How many of this item
            extras: List of extras like 'Almond Milk', 'Extra Shot', 'Vanilla Syrup'
        
        Returns:
            Confirmation message with item details and price
        """
        logger.info(f"Adding to order: {quantity}x {name} ({size}) with extras: {extras}")
        
        # Validate category
        if category not in MENU:
            return f"Sorry, I don't recognize the category '{category}'. Please use 'coffee', 'tea', or 'pastries'."
        
        # Validate item exists
        if name not in MENU[category]:
            available = ", ".join(MENU[category].keys())
            return f"Sorry, we don't have '{name}'. Available {category}: {available}"
        
        # Create order item
        item = OrderItem(
            category=category,
            name=name,
            size=size.upper() if category in ["coffee", "tea"] else "N/A",
            quantity=quantity,
            extras=extras or [],
        )
        
        # Add to order
        self.current_order.add_item(item)
        
        # Format confirmation
        extras_str = f" with {', '.join(item.extras)}" if item.extras else ""
        size_str = f" ({item.size})" if category in ["coffee", "tea"] else ""
        
        return f"Added {quantity}x {name}{size_str}{extras_str} for ${item.price:.2f}. Anything else?"

    @function_tool
    async def get_order_summary(self, context: RunContext) -> str:
        """Get a summary of the current order. Use this when customer wants to review their order or before finalizing.
        
        Returns:
            Complete order summary with total price
        """
        logger.info("Getting order summary")
        summary = self.current_order.get_summary()
        
        if self.current_order.customer_name:
            summary = f"Order for {self.current_order.customer_name}:\n" + summary
        
        return summary

    @function_tool
    async def set_customer_name(self, context: RunContext, name: Annotated[str, "Customer's name for the order"]) -> str:
        """Set the customer's name for the order. Use this when they provide their name.
        
        Args:
            name: The customer's name
        
        Returns:
            Confirmation message
        """
        logger.info(f"Setting customer name: {name}")
        self.current_order.customer_name = name
        return f"Perfect! I've got this order for {name}."

    @function_tool
    async def remove_item_from_order(self, context: RunContext, item_number: Annotated[int, "Item number to remove (1-based index)"]) -> str:
        """Remove an item from the order. Use this when customer wants to remove or change something.
        
        Args:
            item_number: The item number to remove (starting from 1)
        
        Returns:
            Confirmation of removal
        """
        logger.info(f"Removing item {item_number} from order")
        
        if not self.current_order.items:
            return "There are no items in the order to remove."
        
        if item_number < 1 or item_number > len(self.current_order.items):
            return f"Invalid item number. Please choose between 1 and {len(self.current_order.items)}."
        
        removed_item = self.current_order.items.pop(item_number - 1)
        return f"Removed {removed_item.name} from your order."

    @function_tool
    async def finalize_order(self, context: RunContext) -> str:
        """Finalize the order and prepare for payment. Use this after confirming all items and getting customer name.
        
        Returns:
            Final order confirmation with total and next steps
        """
        logger.info("Finalizing order")
        
        if not self.current_order.items:
            return "I don't have any items in your order yet. What would you like to order?"
        
        if not self.current_order.customer_name:
            return "I still need your name for the order. What name should I put this under?"
        
        total = self.current_order.get_total()
        summary = self.current_order.get_summary()
        
        return f"{summary}\n\nYour order is ready! Please proceed to payment. We'll have your order ready shortly, {self.current_order.customer_name}. Thank you for visiting Brew Haven Café!"


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    # Logging setup
    # Add any other context you want in all log entries here
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    # Set up a voice AI pipeline using OpenAI, Cartesia, AssemblyAI, and the LiveKit turn detector
    session = AgentSession(
        # Speech-to-text (STT) is your agent's ears, turning the user's speech into text that the LLM can understand
        # See all available models at https://docs.livekit.io/agents/models/stt/
        stt=deepgram.STT(model="nova-3"),
        # A Large Language Model (LLM) is your agent's brain, processing user input and generating a response
        # See all available models at https://docs.livekit.io/agents/models/llm/
        llm=google.LLM(
                model="gemini-2.5-flash",
            ),
        # Text-to-speech (TTS) is your agent's voice, turning the LLM's text into speech that the user can hear
        # See all available models as well as voice selections at https://docs.livekit.io/agents/models/tts/
        tts=murf.TTS(
                voice="en-US-matthew", 
                style="Conversation",
                tokenizer=tokenize.basic.SentenceTokenizer(min_sentence_len=2),
                text_pacing=True
            ),
        # VAD and turn detection are used to determine when the user is speaking and when the agent should respond
        # See more at https://docs.livekit.io/agents/build/turns
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
        # allow the LLM to generate a response while waiting for the end of turn
        # See more at https://docs.livekit.io/agents/build/audio/#preemptive-generation
        preemptive_generation=True,
    )

    # To use a realtime model instead of a voice pipeline, use the following session setup instead.
    # (Note: This is for the OpenAI Realtime API. For other providers, see https://docs.livekit.io/agents/models/realtime/))
    # 1. Install livekit-agents[openai]
    # 2. Set OPENAI_API_KEY in .env.local
    # 3. Add `from livekit.plugins import openai` to the top of this file
    # 4. Use the following session setup instead of the version above
    # session = AgentSession(
    #     llm=openai.realtime.RealtimeModel(voice="marin")
    # )

    # Metrics collection, to measure pipeline performance
    # For more information, see https://docs.livekit.io/agents/build/metrics/
    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    ctx.add_shutdown_callback(log_usage)

    # # Add a virtual avatar to the session, if desired
    # # For other providers, see https://docs.livekit.io/agents/models/avatar/
    # avatar = hedra.AvatarSession(
    #   avatar_id="...",  # See https://docs.livekit.io/agents/models/avatar/plugins/hedra
    # )
    # # Start the avatar and wait for it to join
    # await avatar.start(session, room=ctx.room)

    # Start the session, which initializes the voice pipeline and warms up the models
    await session.start(
        agent=CoffeeBarista(),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # Join the room and connect to the user
    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
