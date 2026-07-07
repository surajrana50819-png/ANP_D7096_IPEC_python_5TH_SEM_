# Lab 4: Inventory Management
# Problem: Dictionary to maintain stock of products

inventory = {}
n = int(input("Enter number of products: "))
for i in range(n):
    product = input("Enter product name: ")
    qty = int(input(f"Enter stock of {product}: "))
    inventory[product] = qty

# ---- Add new product
new_product = input("Enter new product name: ")
new_qty = int(input(f"Enter stock of {new_product}: "))
inventory[new_product] = new_qty
print("After Adding:", inventory)

# ---- Update stock
update_product = input("Enter product name to update stock: ")
if update_product in inventory:
    inventory[update_product] = int(input("Enter new stock: "))
print("After Updating:", inventory)

# ---- Remove product
remove_product = input("Enter product name to remove: ")
if remove_product in inventory:
    del inventory[remove_product]
print("After Removing:", inventory)

# ---- Display products with stock < 20
print("Products with stock < 20:")
for item, qty in inventory.items():
    if qty < 20:
        print(item, ":", qty)

# ---- Display total items in inventory
total_items = sum(inventory.values())
print("Total Items in Inventory:", total_items)
