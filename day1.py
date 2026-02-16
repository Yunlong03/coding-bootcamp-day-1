# Interactive Product Search and Pricing Calculator
import random

# Get user input
user_name = input("What's your name? ")
print("Welcome to the store, " + user_name + "!")

# Product search input
product_name = input("\nWhat product are you searching for? ")
product_category = input("What category is it in? ")
print("\nYou searched for: " + product_name)
print("Category: " + product_category)

# Random pricing between 333 and 666
original_price = random.uniform(333, 666)
original_price = round(original_price, 2)  # Round to 2 decimal places

# Fixed discount
discount_percentage = 25

# Calculate discount amount
discount_amount = original_price * (discount_percentage / 100)

# Calculate final price after discount
final_price = original_price - discount_amount

# Display pricing details
print("\n--- Pricing Breakdown ---")
print("Original Price: $" + str(original_price))
print("Discount: " + str(discount_percentage) + "%")
print("You Save: $" + str(discount_amount))
print("Final Price After Discount: $" + str(final_price))

# Calculate shipping (10% of discounted price)
shipping_percentage = 10
shipping_cost = final_price * (shipping_percentage / 100)
price_with_shipping = final_price + shipping_cost

print("\n--- Shipping ---")
print("Shipping (" + str(shipping_percentage) + "%): $" + str(shipping_cost))
print("Price with Shipping: $" + str(price_with_shipping))

# Calculate tax (8% of price including shipping)
tax_rate = 8
tax_amount = price_with_shipping * (tax_rate / 100)
total_with_tax = price_with_shipping + tax_amount

print("\n--- Final Total ---")
print("Tax (" + str(tax_rate) + "%): $" + str(tax_amount))
print("TOTAL PRICE: $" + str(total_with_tax))

