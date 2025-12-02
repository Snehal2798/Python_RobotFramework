#You’re building a simple billing system for a grocery store. A customer picks two items and the cashier needs to calculate the total cost by adding the prices of the two items.
#Your task is to create a program that:
#Takes input of two item prices from the user.
#Adds the two numbers.
#Displays the total amount the customer needs to pay.

# Taking input prices from the user
print("*************GROCERY STORE*******************")
price1 = float(input("Enter the price of the first item: "))
price2 = float(input("Enter the price of the second item: "))

# Calculating total
total = price1 + price2

# Displaying the final bill
print("Total amount to pay:", total)