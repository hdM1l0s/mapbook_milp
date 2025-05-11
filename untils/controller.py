def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy{user['name']}, z miejscowości: {user['Location']} opublikował {user['posts']} postów")


def add_user(users_data: list) -> None:
    new_name = input('podaj imie nowego uzytkownika')
    new_location = input('podaj lokalizacje uztykownika')
    new_posts = int(input('podaj liczbe postow nowego uztykownika'))
    users_data.append({"name": new_name, "Location": new_location, "posts": new_posts}, )


def remove_user(users_data: list) -> None:
    uzytkownik_do_usuniecia = input('podaj uzytkownika do usuniecia: ')

    for user in users_data:
        if user['name'] == uzytkownik_do_usuniecia:
            users_data.remove(user)
def update_user(users_data:list)->None:
    uzytkownik_do_usuniecia = input('podaj uzytkownika do edeycji: ')
    for user in users_data:
        if user['name'] == uzytkownik_do_usuniecia:
            user['name']=input('podaj nowe imie uzytkownika: ')
            user['Location']=input('podaj nowa lokazlizacje uzytkownika: ')
            user['posts']=int (input('podaj liczbe postow: '))