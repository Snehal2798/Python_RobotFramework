#You are designing a social media signup form, and each platform has rules for usernames. One of the common rules is that a username must be between a certain number of characters — not too short, not too long.
#To help enforce this rule, you need a program that:
#Accepts a username from the user.
#Calculates the length of the username.
#Displays the length.
#Optionally tells the user whether the username is too short, too long, or acceptable.

# Accept username from the user
username = input("Enter a username: ")

# Calculate length
length = len(username)

# Display the length
print(f"Your username is {length} characters long.")
# Set your platform rules
min_length = 5
max_length = 15

# Check if it's acceptable
if length < min_length:
    print("❗ Username is too short.")
elif length > max_length:
    print("❗ Username is too long.")
else:
    print("✔️ Username length is acceptable.")
