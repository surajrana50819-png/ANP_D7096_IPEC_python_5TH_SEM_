
# Program using tuples for product prices

# List of products as tuples (name, price)
products = [
    ("Headset", 2450),
    ("iphone", 140000),
    ("mouse", 415),
    ("keyboard ", 1000),
    ("sticker", 10),
    ("screen", 1300)
    ("")
]

# Find the lowest price
lowest_price = min(price for _, price in products)

# Count how many products have price = 10
count_price_10 = sum(1 for _, price in products if price == 10)

# Display results
print("Product List with Prices:")
for name, price in products:
    print(f"{name}: {price}")

print("\nLowest Price:", lowest_price)
print("Number of products with price 10:", count_price_10)