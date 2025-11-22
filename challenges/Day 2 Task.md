# Day 2 – Coffee Shop Barista Agent

## Objective

Build a voice agent that acts as a friendly coffee shop barista, capable of:

- Taking customer orders for coffee, tea, and pastries
- Managing a menu with different sizes and customizations
- Adding extras like milk alternatives and syrups
- Tracking the complete order with pricing
- Confirming orders with customer name

## Features Implemented

### 1. **Interactive Menu System**

- Coffee drinks (Espresso, Latte, Cappuccino, Mocha, etc.)
- Tea options (Green Tea, Chai Latte, Herbal Tea, etc.)
- Pastries (Croissants, Muffins, Cookies, etc.)
- Extras (Milk alternatives, Syrups, Extra shots)

### 2. **Function Tools**

- `get_menu()` - Display menu categories
- `add_item_to_order()` - Add items with size, quantity, and extras
- `get_order_summary()` - Review current order
- `set_customer_name()` - Set name for the order
- `remove_item_from_order()` - Modify order by removing items
- `finalize_order()` - Complete the order and confirm total

### 3. **State Management**

- Order tracking with dataclasses
- Price calculations including extras
- Customer name association
- Multi-item order support

### 4. **Natural Conversation Flow**

- Greeting and welcome
- Menu recommendations
- Size selection
- Extras suggestions
- Order confirmation
- Payment handoff

## How to Run

1. **Start the backend:**

```bash
cd backend
uv run python src/agent.py dev
```

2. **Start the frontend:**

```bash
cd frontend
pnpm dev
```

3. **Start LiveKit server** (if not already running):

```bash
livekit-server --dev
```

4. Open http://localhost:3000 and start ordering coffee!

## Example Conversation

**Barista:** "Welcome to Brew Haven Café! I'm Bella, your barista today. What can I get started for you?"

**Customer:** "Hi! What coffee do you have?"

**Barista:** _Shows menu_ "We have Espresso, Americano, Latte, Cappuccino, Mocha, Flat White, and Macchiato. What sounds good to you?"

**Customer:** "I'll have a large latte with oat milk"

**Barista:** "Added 1x Latte (L) with Oat Milk for $5.00. Anything else?"

**Customer:** "Yes, add a chocolate muffin too"

**Barista:** "Added 1x Chocolate Muffin for $3.75. Anything else?"

**Customer:** "That's all"

**Barista:** "Perfect! Can I get your name for the order?"

**Customer:** "Sarah"

**Barista:** _Reviews order_ "Great Sarah! Your total is $8.75. Please proceed to payment..."

## Technical Highlights

- **LiveKit Agents Framework** with Murf Falcon TTS
- **Function tools** for structured order management
- **Dataclasses** for type-safe order state
- **Dynamic pricing** based on size and extras
- **Error handling** for invalid menu items
- **Voice-optimized responses** without formatting

## Next Steps

- Add payment integration
- Implement order modification (change size/extras)
- Add loyalty program support
- Create custom frontend with coffee shop branding
- Add voice feedback for order confirmation

---

**Built for the Murf AI Voice Agents Challenge - Day 2**
