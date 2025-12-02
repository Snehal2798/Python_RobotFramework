#Your job is to write a program that:
#Takes a ticket number as input.
#Uses a function to check if the number is even or odd.
#Displays which gate the person should go to.
#Objectives:Take user input for the ticket number.
#Use a function to check if the number is even or odd.
#Display which gate the person should enter from.

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0   # returns True if even, False if odd

# --- Main program starts here ---

# Ask the user for their ticket number
ticket_number = int(input("Enter your ticket number: "))

# Call the function to check even/odd
if is_even(ticket_number):
    print("Please proceed to Gate A (Even-numbered tickets).")
else:
    print("Please proceed to Gate B (Odd-numbered tickets).")