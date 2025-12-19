#You’ve been hired to help build a puzzle game that includes a secret code challenge. In one level, players must enter a magic word that is the same when read forwards and backwards — a palindrome — to unlock the next clue.
#Your job is to write a program that:
#Accepts a word (or sentence) from the player.
#Checks if it is a palindrome using string manipulation.

# Accept input from the player
text = input("Enter the magic word: ")

# Remove spaces and convert to lowercase for fair comparison
cleaned = text.replace(" ", "").lower()

# Check if it's a palindrome
if cleaned == cleaned[::-1]:
    print("✨ Correct! The word is a palindrome.")
else:
    print("❌ Not a palindrome. Try again!")