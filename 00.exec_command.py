import os
from subprocess import call

def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux
        os.system('clear')

def import_config():
    file_path = input("Path File Wireguard: ")
    try:
        call(['sudo', 'nmcli', 'connection', 'import', 'type', 'wireguard', 'file', file_path])
    except Exception as e:
        print(f"An error occurred while importing the configuration file: {e}")

def show_config():
    try:
        call(['sudo', 'nmcli', 'connection', 'show'])
    except Exception as e:
        print(f"An error occurred while showing the configuration: {e}")

def delete_config():
    connection_id = input("ID of the connection you want to delete: ")
    try:
        call(['sudo', 'nmcli', 'connection', 'delete', connection_id])
    except Exception as e:
        print(f"An error occurred while deleting the connection: {e}")

def main_menu():
    while True:
        print("Menu: \n 1. Import config \n 2. Show config \n 3. Delete config \n 4. Closing the program")
        user_input = input("Enter the number of the menu: ")
        clear_screen()
        if user_input == "1":
            import_config()
        elif user_input == "2":
            show_config()
        elif user_input == "3":
            delete_config()
        else:
            print("Closing the program.")
            break
        input(" ")
        clear_screen()

main_menu()