# 🧪 Testing Guide - Coffee Shop Barista Agent

## Quick Test Scenarios

### Scenario 1: Simple Coffee Order ☕

**Goal**: Test basic ordering flow

```
Customer: "Hi!"
Expected: Greeting from Bella, mention of Brew Haven Café

Customer: "I want a medium latte"
Expected:
- Tool call: add_item_to_order(category="coffee", name="Latte", size="M")
- Response: "Added 1x Latte (M) for $4.00. Anything else?"

Customer: "No, that's all"
Expected: Asks for name

Customer: "John"
Expected:
- Tool call: set_customer_name(name="John")
- Order summary with total

Customer: "Yes"
Expected:
- Tool call: finalize_order()
- Confirmation and thank you
```

### Scenario 2: Complex Order with Customizations 🥤

**Goal**: Test size selection, extras, and multiple items

```
Customer: "What coffee do you have?"
Expected:
- Tool call: get_menu(category="coffee")
- Lists: Espresso, Americano, Latte, Cappuccino, Mocha, Flat White, Macchiato

Customer: "I'll take a large mocha with oat milk and whipped cream"
Expected:
- Tool call: add_item_to_order(category="coffee", name="Mocha", size="L", extras=["Oat Milk", "Whipped Cream"])
- Response: "Added 1x Mocha (L) with Oat Milk, Whipped Cream for $6.00. Anything else?"

Customer: "Also a croissant"
Expected:
- Tool call: add_item_to_order(category="pastries", name="Croissant")
- Response: "Added 1x Croissant for $3.50. Anything else?"

Customer: "That's it. Name is Sarah"
Expected:
- Tool call: set_customer_name(name="Sarah")
- Tool call: get_order_summary()
- Shows both items with total $9.50
```

### Scenario 3: Menu Exploration 📋

**Goal**: Test menu browsing

```
Customer: "Show me the full menu"
Expected:
- Tool call: get_menu(category="all")
- Lists all categories: coffee, tea, pastries, extras

Customer: "What teas do you have?"
Expected:
- Tool call: get_menu(category="tea")
- Lists: Green Tea, Black Tea, Chai Latte, Herbal Tea

Customer: "What extras can I add?"
Expected:
- Tool call: get_menu(category="extras")
- Lists: Extra Shot, Almond/Oat/Soy Milk, Syrups, Whipped Cream
```

### Scenario 4: Order Modification ✏️

**Goal**: Test removing items

```
Customer: "I want a latte and a cappuccino"
Expected: Adds both items

Customer: "Actually, remove the cappuccino"
Expected:
- Tool call: remove_item_from_order(item_number=2)
- Response: "Removed Cappuccino from your order"

Customer: "Show me my order"
Expected:
- Tool call: get_order_summary()
- Shows only latte
```

### Scenario 5: Multiple Quantities 🔢

**Goal**: Test quantity handling

```
Customer: "I need three large americanos"
Expected:
- Tool call: add_item_to_order(category="coffee", name="Americano", size="L", quantity=3)
- Response: "Added 3x Americano (L) for $12.00. Anything else?"
```

## Expected Function Tool Calls

### 1. get_menu

**When**: Customer asks about menu, wants to see options
**Parameters**:

- `category`: "all", "coffee", "tea", "pastries", "extras"

**Test cases**:

```python
✅ "What do you have?" → get_menu(category="all")
✅ "Show me coffee" → get_menu(category="coffee")
✅ "What pastries?" → get_menu(category="pastries")
```

### 2. add_item_to_order

**When**: Customer orders an item
**Parameters**:

- `category`: "coffee", "tea", "pastries"
- `name`: Exact menu item name
- `size`: "S", "M", "L" (coffee/tea only)
- `quantity`: Integer (default 1)
- `extras`: List of extra items

**Test cases**:

```python
✅ "Medium latte" → add_item_to_order(category="coffee", name="Latte", size="M")
✅ "Large latte with oat milk" → add_item_to_order(category="coffee", name="Latte", size="L", extras=["Oat Milk"])
✅ "Two croissants" → add_item_to_order(category="pastries", name="Croissant", quantity=2)
```

### 3. get_order_summary

**When**: Customer wants to review order, or before finalizing
**Parameters**: None

**Test cases**:

```python
✅ "What's in my order?" → get_order_summary()
✅ "Show me total" → get_order_summary()
✅ "Review order" → get_order_summary()
```

### 4. set_customer_name

**When**: Customer provides their name
**Parameters**:

- `name`: Customer's name string

**Test cases**:

```python
✅ "My name is Alex" → set_customer_name(name="Alex")
✅ "Sarah" (in response to name question) → set_customer_name(name="Sarah")
```

### 5. remove_item_from_order

**When**: Customer wants to remove something
**Parameters**:

- `item_number`: Integer (1-based index)

**Test cases**:

```python
✅ "Remove the latte" → remove_item_from_order(item_number=1)
✅ "Take off the second item" → remove_item_from_order(item_number=2)
```

### 6. finalize_order

**When**: Order is complete and name is provided
**Parameters**: None

**Test cases**:

```python
✅ After name + confirmation → finalize_order()
✅ "Complete the order" → finalize_order()
```

## Price Calculation Tests

### Coffee Sizes

```
Espresso:    S=$2.50, M=$3.00, L=$3.50
Americano:   S=$3.00, M=$3.50, L=$4.00
Latte:       S=$3.50, M=$4.00, L=$4.50
Cappuccino:  S=$3.50, M=$4.00, L=$4.50
Mocha:       S=$4.00, M=$4.50, L=$5.00
Flat White:  S=$3.75, M=$4.25, L=$4.75
Macchiato:   S=$3.25, M=$3.75, L=$4.25
```

### Extras Pricing

```
Extra Shot:       +$0.75
Almond Milk:      +$0.50
Oat Milk:         +$0.50
Soy Milk:         +$0.50
Whipped Cream:    +$0.50
Vanilla Syrup:    +$0.50
Caramel Syrup:    +$0.50
Hazelnut Syrup:   +$0.50
```

### Example Calculations

```
✅ Large Latte = $4.50
✅ Large Latte + Oat Milk = $4.50 + $0.50 = $5.00
✅ Large Mocha + Oat Milk + Whipped Cream = $5.00 + $0.50 + $0.50 = $6.00
✅ 2x Medium Americano = $3.50 × 2 = $7.00
✅ Croissant = $3.50
✅ Cookie = $2.50
```

## Edge Cases to Test

### 1. Invalid Item

```
Customer: "I want a burger"
Expected: Agent explains they don't have that, suggests coffee/tea/pastries
```

### 2. Invalid Size

```
Customer: "Extra large espresso"
Expected: Agent asks to choose S, M, or L
```

### 3. Empty Order

```
Customer: "Finalize my order"
Expected: Agent says no items in order yet
```

### 4. No Name Provided

```
Customer: "Complete order" (without giving name)
Expected: Agent asks for name
```

### 5. Unclear Request

```
Customer: "Something sweet"
Expected: Agent suggests pastries or sweetened drinks
```

## Running Automated Tests

### Unit Tests

```bash
cd backend
uv run pytest tests/test_agent.py -v
```

**Expected tests**:

- `test_offers_assistance` - Greeting test
- `test_menu_display` - Menu functionality
- `test_takes_coffee_order` - Order processing

### Manual Voice Testing

1. Start all services (LiveKit + Backend + Frontend)
2. Open http://localhost:3000
3. Click "Start Ordering ☕"
4. Run through each scenario above
5. Verify:
   - ✅ Correct tool calls
   - ✅ Accurate pricing
   - ✅ Natural conversation
   - ✅ Order summary
   - ✅ Finalization works

## Success Metrics

Your agent is working correctly if:

- ✅ **Greeting**: Introduces as Bella from Brew Haven Café
- ✅ **Menu Display**: Shows correct items by category
- ✅ **Order Taking**: Adds items with correct details
- ✅ **Pricing**: Calculates totals accurately
- ✅ **Customization**: Handles size and extras
- ✅ **State Management**: Tracks order across conversation
- ✅ **Name Collection**: Asks for and stores customer name
- ✅ **Summary**: Shows complete order review
- ✅ **Finalization**: Completes order with total
- ✅ **Voice Quality**: Fast, natural responses (thanks to Murf Falcon)

## Common Issues & Fixes

### Issue: Agent doesn't call tools

**Fix**: Check LLM has access to function definitions, verify instructions mention tools

### Issue: Wrong prices calculated

**Fix**: Verify MENU dictionary values, check calculate_price() logic

### Issue: Can't remove items

**Fix**: Ensure item numbers are 1-based, check order has items

### Issue: Order state lost between turns

**Fix**: Verify CustomerOrder persists in agent instance

### Issue: No response from agent

**Fix**: Check API keys, verify all services running, check logs

---

**Happy Testing! ☕🧪**
