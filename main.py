users = [
    {"name": "Miłosz", "Location": "Warszawa", "posts": 500},
    {"name": "Michał", "Location": "Krasnystaw", "posts": 400},
    {"name": "Ksavier", "Location": "Grudziąc", "posts": 300},
    {"name": "Damian", "Location": "Kraków", "posts": 200},

]

for user in users:
    print(f"Twój znajomy{user['name']}, z {user['location']} opublikował {user['posts']} postów")
