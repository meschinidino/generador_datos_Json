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

# Function to create a random list of movie objects for each category
def create_movie_list(category_size):
    return [{"movie_id": movie["$oid"]} for movie in random.sample(movie_ids, category_size)]

# Function to generate a home document for a user
def generate_home_document(user_id):
    home_doc = {
        "user_id": user_id,
        "trending": create_movie_list(3),         # Random selection for trending
        "recently_watched": create_movie_list(4), # Random selection for recently watched
        "recommendations": create_movie_list(5),  # Random selection for recommendations
        "watchlist": create_movie_list(3),        # Random selection for watchlist
        "last_updated": "2024-10-28T18:00:00Z"    # Example timestamp
    }
    return home_doc

# Generate 500 home documents for users with IDs 2 through 501
home_collection = [generate_home_document(user_id) for user_id in range(2, 502)]

# Write the generated home documents to a JSON file
with open("home_collection.json", "w") as f:
    json.dump(home_collection, f, indent=4)

print("Home collection JSON data generated successfully!")
