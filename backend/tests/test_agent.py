import pytest
from livekit.agents import AgentSession, inference, llm

from agent import CoffeeBarista


def _llm() -> llm.LLM:
    return inference.LLM(model="openai/gpt-4.1-mini")


@pytest.mark.asyncio
async def test_offers_assistance() -> None:
    """Evaluation of the agent's friendly nature and coffee shop greeting."""
    async with (
        _llm() as llm,
        AgentSession(llm=llm) as session,
    ):
        await session.start(CoffeeBarista())

        # Run an agent turn following the user's greeting
        result = await session.run(user_input="Hello")

        # Evaluate the agent's response for friendliness
        await (
            result.expect.next_event()
            .is_message(role="assistant")
            .judge(
                llm,
                intent="""
                Greets the user warmly as a coffee shop barista.

                Expected elements:
                - Friendly greeting
                - Introduction as Bella, the barista
                - Mention of Brew Haven Café
                - Offer to take their order or help them
                - Enthusiastic and welcoming tone
                """,
            )
        )

        # Ensures there are no function calls or other unexpected events
        result.expect.no_more_events()


@pytest.mark.asyncio
async def test_menu_display() -> None:
    """Evaluation of the agent's ability to display the menu."""
    async with (
        _llm() as llm,
        AgentSession(llm=llm) as session,
    ):
        await session.start(CoffeeBarista())

        # Run an agent turn asking about the menu
        result = await session.run(user_input="What drinks do you have?")

        # Expect a function call to get_menu
        result.expect.next_event().is_function_call(name="get_menu")

        # Evaluate the agent's response about available drinks
        await (
            result.expect.next_event()
            .is_message(role="assistant")
            .judge(
                llm,
                intent="""
                Provides information about available coffee and tea drinks.
                
                Should mention items like:
                - Espresso, Latte, Cappuccino, Mocha, or other coffee drinks
                - May ask what sounds good or offer recommendations
                - Friendly and helpful tone
                """,
            )
        )


@pytest.mark.asyncio
async def test_takes_coffee_order() -> None:
    """Evaluation of the agent's ability to take a coffee order."""
    async with (
        _llm() as llm,
        AgentSession(llm=llm) as session,
    ):
        await session.start(CoffeeBarista())

        # Run an agent turn with a coffee order
        result = await session.run(user_input="I'll have a large latte with oat milk")

        # Expect a function call to add_item_to_order
        result.expect.next_event().is_function_call(name="add_item_to_order")

        # Evaluate the agent's response confirming the order
        await (
            result.expect.next_event()
            .is_message(role="assistant")
            .judge(
                llm,
                intent="""
                Confirms the order was added and asks if they want anything else.
                
                Should include:
                - Confirmation that the latte with oat milk was added
                - The price
                - Question about adding more items
                """,
            )
        )
