import random
import json

first_names = [
    'John', 'Jane', 'Michael', 'Emily', 'Matthew', 'Olivia', 'Daniel', 'Emma',
    'Joshua', 'Sophia', 'David', 'Isabella', 'Jacob', 'Ava', 'Ethan', 'Mia',
    'Andrew', 'Charlotte', 'James', 'Amelia', 'Benjamin', 'Harper', 'Samuel', 'Evelyn',
    'Noah', 'Ella', 'Lucas', 'Lily', 'Henry', 'Grace', 'Alexander', 'Scarlett',
    'Sebastian', 'Madison', 'Logan', 'Luna', 'Jack', 'Zoey', 'Owen', 'Chloe',
    'Ryan', 'Victoria', 'Elijah', 'Penelope', 'Christopher', 'Aubrey', 'Nathan', 'Aria',
    'Zachary', 'Layla', 'Isaac', 'Hannah', 'Thomas', 'Nora'
]

last_names = [
    'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
    'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Taylor',
    'Thomas', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White',
    'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young',
    'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores',
    'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell',
    'Carter', 'Roberts', 'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz', 'Parker'
]

subscriptions = ['Free', 'Premium', 'VIP']


def generate_random_password():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))


def generate_random_users(num_users=1000):
    users = []
    for _ in range(num_users):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        password = generate_random_password()
        subscription = random.choice(subscriptions)
        user = {
            'name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'subscription': subscription
        }
        users.append(user)

    # Write the users to a JSON file
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

    print(f"Generated {num_users} users and saved to 'users.json'")
