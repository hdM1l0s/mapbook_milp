from untils.controller import get_user_info, add_user , remove_user , update_user
from untils.models import users

def main():
    while True:

        print ("===========MENU=============")
        print ("0 - koniec aplikacji")
        print ("1 - wyświetl co u znajomych")
        print ("2 - dodaj nowego użytkownika")
        print ("3 - usuń użytkownika")
        print ("3 - edytuj użytkownika")
        print ("===========MENU=============")


        choice = input("wybierz opcjie menu")
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': update_user(users)




if __name__ == "__main__":
    main()
