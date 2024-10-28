import json
import random

# Movie IDs from your database
movie_ids = [
    {"$oid": "670fb35458642d563dbcb4ec"},
    {"$oid": "670fb35458642d563dbcb4ed"},
    {"$oid": "670fb35458642d563dbcb4ee"},
    {"$oid": "670fb41a58642d563dbcb4f0"},
    {"$oid": "670fb41a58642d563dbcb4f1"},
    {"$oid": "670fb41a58642d563dbcb4f2"},
    {"$oid": "670fb41a58642d563dbcb4f3"},
    {"$oid": "670fb41a58642d563dbcb4f4"},
    {"$oid": "670fb41a58642d563dbcb4f5"},
    {"$oid": "670fb41a58642d563dbcb4f6"},
    {"$oid": "670fb41a58642d563dbcb4f7"},
    {"$oid": "670fb41a58642d563dbcb4f8"},
    {"$oid": "670fb41a58642d563dbcb4f9"}
]

# Function to generate a random list of movie IDs
def generate_movie_list(movie_list, num_movies):
    return [{"movie_id": movie["$oid"]} for movie in random.sample(movie_list, num_movies)]

# Generate 500 playlists, each as an individual object
num_lists = 500               # Number of lists to generate
num_movies_per_list = 5       # Number of movies in each list

movie_collections = [{"movies": generate_movie_list(movie_ids, num_movies_per_list)} for _ in range(num_lists)]

# Write the generated lists to a JSON file
with open("movie_collections.json", "w") as f:
    json.dump(movie_collections, f, indent=4)

print("Movie collections JSON data generated successfully!")
