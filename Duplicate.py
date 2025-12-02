#_duplicate_record - You're helping analyze the results of a student survey where participants were asked to name their favorite movie. Since many students love the same popular movies, some movie titles appear multiple times in the results.
#Your job is to write a program that:
#Accepts a list of favorite movie titles.
#Uses a for loop to count how many times each movie was mentioned.
#Displays only the movie titles that were mentioned more than once.

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