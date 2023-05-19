# Define product prices
product_prices = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Define discount rules
discount_rules = {
    "flat_10_discount": (200, 10),
    "bulk_5_discount": (10, 0.05),
    "bulk_10_discount": (20, 0.1),
    "tiered_50_discount": (30, 0.5)
}

# Define fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
items_per_package = 10

# Initialize variables
subtotal = 0
total_quantity = 0
discount_name = None
discount_amount = 0
product_details = []

# Input quantities and gift wrapping choice for each product
for product_name in product_prices:
    quantity = int(input(f"Enter the quantity of {product_name}: "))
    is_gift_wrapped = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == "yes"
    
    # Calculate product total
    product_total = product_prices[product_name] * quantity
    
    # Apply gift wrap fee
    if is_gift_wrapped:
        product_total += gift_wrap_fee * quantity
    
    # Calculate discount amount for each rule
    for rule_name, (rule_quantity, rule_discount) in discount_rules.items():
        if quantity >= rule_quantity:
            rule_discount_amount = (quantity - rule_quantity) * product_prices[product_name] * rule_discount
            if rule_discount_amount > discount_amount:
                discount_name = rule_name
                discount_amount = rule_discount_amount
    
    # Update subtotal and total quantity
    subtotal += product_total
    total_quantity += quantity
    
    # Add product details to the list
    product_details.append(f"{product_name}: {quantity} - ${product_total}")

# Apply the most beneficial discount
subtotal -= discount_amount

# Calculate shipping fees
shipping_fee = (total_quantity // items_per_package) * shipping_fee_per_package

# Calculate total amount
total = subtotal + shipping_fee

# Output the details
print("\nProduct Details:")
for detail in product_details:
    print(detail)
print(f"\nSubtotal: ${subtotal}")
if discount_name:
    print(f"Discount Applied: {discount_name} - ${discount_amount}")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Total: ${total}")
