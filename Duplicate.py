#You are designing a social media signup form, and each platform has rules for usernames. One of the common rules is that a username must be between a certain number of characters — not too short, not too long.
#To help enforce this rule, you need a program that:
#Accepts a username from the user.
#Calculates the length of the username.
#Displays the length.
#Optionally tells the user whether the username is too short, too long, or acceptable.

# List of favorite movies (example input)
movies = [
    "Inception", "Avatar", "Inception",
    "Titanic", "Avengers", "Avatar",
    "Interstellar", "Titanic", "Inception"
]

# Dictionary to store counts
movie_count = {}

# Count each movie using a for loop
for movie in movies:
    if movie in movie_count:
        movie_count[movie] += 1
    else:
        movie_count[movie] = 1

# Display only movies mentioned more than once
print("Movies mentioned more than once:")
for movie, count in movie_count.items():
    if count > 1:
        print(f"{movie}: {count} times")