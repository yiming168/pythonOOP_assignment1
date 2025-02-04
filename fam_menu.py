from account_types import AccountAngel, AccountTroublemaker, AccountRebel
from budget import Budget

# Mapping user input to subclasses
USER_TYPE = {
    1: AccountAngel,
    2: AccountTroublemaker,
    3: AccountRebel
}

def register_new_user():
    user_name = input("Enter username: ")
    age = int(input("Enter age: "))
    bank_name = input("Enter bank name: ")
    account_num = input("Enter account number: ")
    balance = float(input("Enter balance: "))

    # Display available budget options
    Budget.display_budget_choices()

    # Get the budgets as a comma-separated list
    budgets = list(map(float, input("Enter budgets (comma-separated): ").split(',')))

    # Get user input for account type selection
    user_type_class = None  # Initialize user_type_class before the loop
    while user_type_class is None:
        try:
            user_type_input = int(input("Enter account type number ( 1. Angel, 2. Troublemaker, 3. Rebel): "))
            if user_type_input not in USER_TYPE:
                print("Invalid input. Please select a valid number (1, 2, or 3).")
                continue
            user_type_class = USER_TYPE[user_type_input]  # Assign class after valid input
        except ValueError:
            print("Invalid input. Please enter a valid number (1, 2, or 3).")

    new_account = user_type_class(user_name, age, bank_name, account_num, balance, *budgets)

    FamMenu.ACCOUNT_LIST.append(new_account)

    print(f"Account created successfully: {new_account}")


def list_all_accounts():
    print("\nSelect user to log in as: ")
    for i, account in enumerate(FamMenu.ACCOUNT_LIST):
        lock_status = " - LOCKED" if account.locked_status else ""
        print(f"{i + 1}. {account.user_name} ({account.user_type}){lock_status}")


class FamMenu:

    ACCOUNT_LIST = []
    ACCOUNT_MENU_OPTIONS_NUM = 5

    def __init__(self):
        self._current_login_account = None

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
                    register_new_user()
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

    def login_existing_user(self):
        if not self.ACCOUNT_LIST:
            print("No accounts registered yet. Please register a user first.\n")
            return

        while self._current_login_account is None:
            list_all_accounts()
            selection = self.__get_valid_account_selection()
            selected_account = self.ACCOUNT_LIST[selection - 1]

            if selected_account.locked_status:
                print(f"\n{selected_account.user_name} is LOCKED, they can not login.\n")
                choice = input("Press Enter to continue or 'Q' to return to main menu\n")
                if choice.lower() == 'q':
                    return
                continue
            self._current_login_account = selected_account
        self.view_account_options()

    def __get_valid_account_selection(self):
        while True:
            selection = input("Choose a user to log in as: ")
            try:
                selection = int(selection)
                if 1 <= selection <= len(self.ACCOUNT_LIST):
                    return selection
                else:
                    print("Invalid selection. Please choose a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def view_account_options(self):
        if self.get_current_login_account() is None:
            print("No account selected. Please login to an account first.\n")
            return

        while True:
            print(f"\nLogged in as {self.get_current_login_account().user_name} "
                  f"({self.get_current_login_account().user_type})")
            print("Select from one of the options below:")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transaction by Budget")
            print("4. View Bank Account Details")
            print("5. Logout")
            account_menu_selection = FamMenu._get_valid_account_menu_selection()
            if account_menu_selection == 1:
                self.get_current_login_account().view_budgets()

            elif account_menu_selection == 2:
                self.get_current_login_account().record_transaction()
                if self.get_current_login_account().locked_status:
                    print(f"{self.get_current_login_account().get_user_name()} is LOCKED, "
                          f"you can not log in again until your account is unlocked.")
                    self._current_login_account = None
                    break

            elif account_menu_selection == 3:
                if len(self.get_current_login_account().transactions) == 0:
                    print("\nNo transactions recorded yet.")
                    input("\nPress Enter to continue...")
                    return
                budget_category_selection = Budget.get_valid_budget_category_selection()
                self.get_current_login_account().view_transaction_by_budget(budget_category_selection)

            elif account_menu_selection == 4:
                print(self.get_current_login_account())

            else:
                print("Logging out... You have successfully logged out. Thank you for using FAM!\n")
                self._current_login_account = None
                break

    def _get_valid_account_selection(self):
        while True:
            selection = input("Choose a user to log in as: ")
            try:
                selection = int(selection)
                if 1 <= selection <= len(self.ACCOUNT_LIST):
                    return selection
                else:
                    print("Invalid selection. Please choose a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def _get_valid_account_menu_selection():
        while True:
            selection = input("Choose an account menu option:")
            try:
                selection = int(selection)
                if 1<= selection <= FamMenu.ACCOUNT_MENU_OPTIONS_NUM:
                    return selection
                else:
                    print("Invalid selection. Please choose a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")