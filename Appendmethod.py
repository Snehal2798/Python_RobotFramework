#You’re helping build a simple grocery shopping assistant app. Users can add items they want to buy to a shopping cart (list). Each time the user enters an item, it gets added to the cart using the append() method.
#Your task is to:
#Create an empty list (shopping cart).
#Ask the user to enter items they want to buy.
#Use a loop to append each item to the list.
#Show the final list at the end.

# Create an empty shopping cart list
shopping_cart = []

print("Enter items to add to your shopping cart.")
print("Type 'done' when you are finished.\n")

# Loop to keep adding items
while True:
    item = input("Add item: ")

    if item.lower() == "done":
        break

    # Append the item to the cart
    shopping_cart.append(item)

# Show the final list
print("\nYour shopping cart contains:")
print(shopping_cart)