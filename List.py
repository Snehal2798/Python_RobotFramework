# 1. Create an empty list (shopping cart)
shopping_cart = []

print("Welcome to your Grocery Assistant!")
print("Enter your items. Type 'done' when you are finished.")

# 2. Use a loop to ask for items
while True:
    item = input("Add item: ").strip()

    # Check for the exit word
    if item.lower() == 'done':
        break

    # 3. Append the item to the list
    if item:
        shopping_cart.append(item)
    else:
        print("Empty entries aren't allowed!")

# 4. Show the final list at the end
print("\n--- Final Shopping List ---")

# This part ensures the list is displayed item by item
if len(shopping_cart) > 0:
    for grocery in shopping_cart:
        print(f"- {grocery}")
else:
    print("Your cart is empty.")