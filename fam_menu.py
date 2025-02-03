from typing import List
from account import Account
from account_types import AccountAngel, AccountTroublemaker, AccountRebel
from transaction import Transaction


class FamMenu:

    ACCOUNT_MENU_OPTIONS_NUM = 5

    def __init__(self):
        self._account_list: List[Account] = []
        self._current_login_account = None

    def get_account_list(self):
        return self._account_list

    def get_current_login_account(self):
        return self._current_login_account

    def display_fam_menu(self):
        while True:
            print("Welcome to FAM! Select from the options below:")
            print("1. Register a new user")
            print("2. Login to an existing user")
            print("3. Exit")
            selection = input("Choose an option: ")
            try:
                selection = int(selection)
                if selection == 1:
                    self.register_new_user()
                elif selection == 2:
                    self.login_existing_user()
                elif selection == 3:
                    print("Exiting FAM. Thank you for using FAM. Goodbye!")
                    break
                else:
                    print("Invalid selection. Please choose a valid option.\n")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue

    def register_new_user(self):
        pass

    def login_existing_user(self):
        pass
