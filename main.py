users = [
    {"name": "Miłosz", "Location": "Warszawa", "posts": 500},
    {"name": "Michał", "Location": "Krasnystaw", "posts": 400},
    {"name": "Ksavier", "Location": "Grudziąc", "posts": 300},
    {"name": "Damian", "Location": "Kraków", "posts": 200},

]


def get_user_info(users_data: list)->None:
    for user in users_data:
        print(f"Twój znajomy{user['name']}, z miejscowości: {user['Location']} opublikował {user['posts']} postów")


get_user_info(users)
