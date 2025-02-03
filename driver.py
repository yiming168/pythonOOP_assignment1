from account import Account
from account_types import AccountAngel, AccountTroublemaker, AccountRebel
from transaction import Transaction


def load_test_users():
    # Create Angel user account with transactions
    angel_1_account = AccountAngel("Mickey", 25, "Scotia", "A123456", 2000, 400, 600, 300, 200)
    angel_1_account.transactions.append(Transaction(50, 0, "Blizzard"))
    angel_1_account.transactions.append(Transaction(100, 1, "Zara"))
    angel_1_account.transactions.append(Transaction(100, 2, "Happy Lamb"))
    angel_1_account.transactions.append(Transaction(20, 3, "Dollar Store"))
    angel_1_account.transactions.append(Transaction(30, 0, "Steam"))
    angel_1_account.transactions.append(Transaction(100, 3, "Walmart"))

    # Create TroubleMaker user account with transactions
    troublemaker_1_account = AccountTroublemaker("Garfield", 10, "BMO", "B123456", 1000, 200, 300, 300, 200)
    troublemaker_1_account.transactions.append(Transaction(30, 0, "Steam"))
    troublemaker_1_account.transactions.append(Transaction(1, 1, "Forever 21"))
    troublemaker_1_account.transactions.append(Transaction(80, 2, "Mcdonald"))
    troublemaker_1_account.transactions.append(Transaction(30, 3, "Shoppers"))
    troublemaker_1_account.transactions.append(Transaction(50, 1, "Zara"))

    # Create Rebel user account with transactions
    rebel_1_account = AccountRebel("Snoopy", 12, "TD", "C123456", 800,150, 250, 250, 150)
    rebel_1_account.transactions.append(Transaction(50, 0, "Skating"))
    rebel_1_account.transactions.append(Transaction(50, 1, "Sushi Plus"))
    rebel_1_account.transactions.append(Transaction(50, 2, "Adidas"))
    rebel_1_account.transactions.append(Transaction(50, 3, "Canadian Tire"))
    rebel_1_account.transactions.append(Transaction(50, 1, "Boston Pizza"))

    # Add all accounts to the account list
    Account.account_list.extend([angel_1_account, troublemaker_1_account, rebel_1_account])

def main():
    load_test_users()
    print(Account.account_list[1])
    print(Account.account_list[0])
    print(Account.account_list[2])

    # while True:
    #     print("Welcome to FAM! Select from the options below:")
    #     print("1. Register a new user")
    #     print("2. Login to an existing user")
    #     print("3. Exit")
    #     selection = input("Choose an option: ")
    #     try:
    #         selection = int(selection)
    #         if selection == 1:
    #             register_new_user()
    #         elif selection == 2:
    #             login_existing_user()
    #         elif selection == 3:
    #             print("Exiting FAM. Thank you for using FAM. Goodbye!")
    #             break
    #         else:
    #             print("Invalid selection. Please choose a valid option.\n")
    #             continue
    #     except ValueError:
    #         print("Invalid input. Please enter a number.\n")
    #         continue


if __name__ == '__main__':
    main()

