# ☕ Day 2 - Coffee Shop Barista Agent

## 🎯 Challenge Completed!

A fully functional **AI Coffee Shop Barista** that takes orders via voice using:

- **LiveKit Agents Framework**
- **Murf Falcon TTS** (fastest TTS API)
- **Google Gemini 2.5 Flash** (LLM)
- **Deepgram Nova-3** (STT)

## 🌟 Features

### 🔧 Function Tools Implemented

1. **`get_menu()`** - Browse menu by category (coffee, tea, pastries, extras)
2. **`add_item_to_order()`** - Add items with size, quantity, and customizations
3. **`get_order_summary()`** - Review complete order with pricing
4. **`set_customer_name()`** - Personalize the order
5. **`remove_item_from_order()`** - Modify orders on the fly
6. **`finalize_order()`** - Complete order and proceed to payment

### 📋 Menu

- **Coffee**: Espresso, Americano, Latte, Cappuccino, Mocha, Flat White, Macchiato
- **Tea**: Green Tea, Black Tea, Chai Latte, Herbal Tea
- **Pastries**: Croissant, Muffins, Cinnamon Roll, Banana Bread, Cookie
- **Extras**: Milk alternatives (Almond, Oat, Soy), Syrups (Vanilla, Caramel, Hazelnut), Extra Shot, Whipped Cream

### 💰 Smart Pricing

- Dynamic pricing based on size (S/M/L)
- Automatic calculation of extras
- Real-time order total tracking

## 🚀 Quick Start

### 1. Start LiveKit Server (Terminal 1)

```bash
livekit-server --dev
```

### 2. Start Backend Agent (Terminal 2)

```bash
cd backend
uv run python src/agent.py dev
```

### 3. Start Frontend (Terminal 3)

```bash
cd frontend
pnpm dev
```

### 4. Open Browser

Navigate to: **http://localhost:3000**

Click "Start Ordering ☕" and talk to Bella, your AI barista!

## 🗣️ Example Conversation

```
👤 Customer: "Hi there!"
🤖 Bella: "Welcome to Brew Haven Café! I'm Bella, your barista today.
          What can I get started for you?"

👤 Customer: "What coffee drinks do you have?"
🤖 Bella: [Shows menu] "We have Espresso, Americano, Latte, Cappuccino,
          Mocha, Flat White, and Macchiato. What sounds good?"

👤 Customer: "I'll take a large latte with oat milk"
🤖 Bella: "Added 1x Latte (L) with Oat Milk for $5.00. Anything else?"

👤 Customer: "Yeah, add a chocolate muffin"
🤖 Bella: "Added 1x Chocolate Muffin for $3.75. Anything else?"

👤 Customer: "No, that's it"
🤖 Bella: "Perfect! Can I get your name for the order?"

👤 Customer: "Alex"
🤖 Bella: "Great Alex! Let me confirm your order:
          1. 1x Latte (L) with Oat Milk - $5.00
          2. 1x Chocolate Muffin - $3.75

          Total: $8.75

          Please proceed to payment. We'll have your order ready shortly!"
```

## 🎨 Frontend Customization

The frontend has been themed for a coffee shop experience:

- Coffee brown color scheme (#8B4513)
- Custom welcome message
- Coffee cup icon
- "Start Ordering ☕" button

## 🛠️ Technical Implementation

### State Management

```python
@dataclass
class OrderItem:
    category: str
    name: str
    size: str = "M"
    quantity: int = 1
    extras: list[str] = field(default_factory=list)
    price: float = 0.0

@dataclass
class CustomerOrder:
    items: list[OrderItem] = field(default_factory=list)
    customer_name: str = ""
```

### Agent Personality

- Name: **Bella**
- Location: **Brew Haven Café**
- Traits: Warm, welcoming, knowledgeable, efficient
- Voice-optimized responses (no emojis or formatting)

### Key Technologies

- **LiveKit Agents SDK** - Voice pipeline orchestration
- **Murf Falcon** - Ultra-fast TTS (text-to-speech)
- **Gemini 2.5 Flash** - LLM for conversation
- **Deepgram Nova-3** - STT (speech-to-text)
- **Function Tools** - Structured order management

## 📹 Recording Your Demo

### What to Include

1. **Introduction**: "Hi, I'm [name] and today I built a coffee shop barista voice agent"
2. **Show the Welcome Screen**: Brew Haven Café interface
3. **Start a Conversation**: Click "Start Ordering ☕"
4. **Demo the Features**:
   - Ask about the menu
   - Order a coffee drink with customizations
   - Add a pastry
   - Give your name
   - Review the order summary
5. **Highlight Key Points**:
   - "Using Murf Falcon - the fastest TTS API"
   - "Built with LiveKit Agents Framework"
   - "Natural conversation with function tools"

### LinkedIn Post Template

```
🚀 Day 2 of the Murf AI Voice Agents Challenge! ☕

Today I built an AI Coffee Shop Barista that takes orders via voice!

Features:
✅ Interactive menu browsing
✅ Order customization (sizes, milk alternatives, extras)
✅ Real-time price calculation
✅ Natural conversation flow
✅ Order summary and confirmation

Powered by:
🔥 Murf Falcon - the fastest TTS API
🤖 LiveKit Agents Framework
💡 Google Gemini 2.5 Flash

The agent uses function tools to manage state, handle complex orders,
and provide a seamless coffee ordering experience - just like a real
barista!

#MurfAIVoiceAgentsChallenge #10DaysofAIVoiceAgents #VoiceAI #AI
#LiveKit #MurfFalcon #CoffeeShop

Tag: @Murf AI @Starbucks @[Your favorite coffee brand]

[Video Demo]
```

## 🎯 Challenge Submission

1. ✅ Complete the implementation (Done!)
2. 📹 Record video demo
3. 📱 Post on LinkedIn before 9 PM IST tomorrow
4. 📝 Submit: https://forms.gle/ge58Ne66wfPN98Pg7

## 🔗 Resources Used

- [LiveKit Agents - Tools](https://docs.livekit.io/agents/build/tools/)
- [LiveKit Agents - State Handoffs](https://docs.livekit.io/agents/build/agents-handoffs/#passing-state)
- [LiveKit Agents - Tasks](https://docs.livekit.io/agents/build/tasks/)
- [Drive-Thru Example](https://github.com/livekit/agents/blob/main/examples/drive-thru/agent.py)

## 💡 Next Steps / Improvements

- Add payment integration
- Implement order history
- Add loyalty rewards program
- Support multiple languages
- Add order modification (change size after ordering)
- Integrate with POS system
- Add estimated wait time
- Support dietary preferences/allergies

---

**Built for the Murf AI Voice Agents Challenge - Day 2**  
**Using the fastest TTS API - Murf Falcon** 🚀
