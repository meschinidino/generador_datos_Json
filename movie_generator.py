import random
import json

movie_names = [
    'The Lost Journey', 'Echoes of Time', 'Whispers in the Dark', 'Beneath the Stars',
    'The Final Hour', 'A New Dawn', 'Silent Waters', 'Shadows of Fate', 'Forgotten Memories',
    'The Broken Crown', 'Edge of Reality', 'The Hidden Path', 'Beyond the Horizon',
    'The Crimson Tide', 'Echoes of War', 'The Last Stand', 'Chasing Destiny', 'Fallen Heroes',
    'The Silver Lining', 'Ghosts of the Past'
]

actors = [
    'Tom Hanks', 'Leonardo DiCaprio', 'Scarlett Johansson', 'Morgan Freeman', 'Brad Pitt',
    'Jennifer Lawrence', 'Natalie Portman', 'Denzel Washington', 'Anne Hathaway', 'Meryl Streep',
    'Will Smith', 'Emma Stone', 'Ryan Gosling', 'Robert Downey Jr.', 'Chris Hemsworth',
    'Mark Ruffalo', 'Gal Gadot', 'Hugh Jackman', 'Chris Pratt', 'Johnny Depp', 'Keanu Reeves'
]

genres = ['Action', 'Comedy', 'Drama', 'Thriller', 'Science Fiction', 'Fantasy', 'Horror', 'Romance']

directors = [
    'Steven Spielberg', 'Christopher Nolan', 'Martin Scorsese', 'Quentin Tarantino', 'James Cameron',
    'Ridley Scott', 'Peter Jackson', 'Francis Ford Coppola', 'Clint Eastwood', 'Wes Anderson',
    'Denis Villeneuve', 'Alfred Hitchcock', 'Tim Burton', 'David Fincher'
]


def generate_random_movies(num_movies=100):
    movies = []
    for _ in range(num_movies):
        movie_name = random.choice(movie_names)
        movie_actors = random.sample(actors, k=3)
        genre = random.choice(genres)
        director = random.choice(directors)
        imdb_rating = round(random.uniform(5.0, 9.9), 1)
        movie_length = random.randint(90, 180)
        description = " ".join(random.sample("Lorem ipsum dolor sit amet consectetur adipiscing elit".split(), 5))

        movie = {
            'movie_name': movie_name,
            'actors': movie_actors,
            'genre': genre,
            'director': director,
            'imdb_rating': imdb_rating,
            'movie_length': f'{movie_length} minutes',
            'description': description
        }
        movies.append(movie)

    # Write the movies to a JSON file
    with open('movies.json', 'w') as f:
        json.dump(movies, f, indent=4)

    print(f"Generated {num_movies} movies and saved to 'movies.json'")
