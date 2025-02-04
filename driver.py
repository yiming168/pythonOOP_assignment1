from account_types import AccountAngel, AccountTroublemaker, AccountRebel
from fam_menu import FamMenu
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
    FamMenu.ACCOUNT_LIST.append(angel_1_account)
    FamMenu.ACCOUNT_LIST.append(troublemaker_1_account)
    FamMenu.ACCOUNT_LIST.append(rebel_1_account)

def main():
    load_test_users()

    fam_menu = FamMenu()

    fam_menu.display_fam_menu()

if __name__ == '__main__':
    main()

