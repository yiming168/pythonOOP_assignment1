from transaction import Transaction
from user import User
from budget import Budget

def create_user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    user = User(name, age)
    return user

def main():
    budget = Budget()
    print(budget.get_budget_detail())
    trans = Transaction(50,1,"dfasdfashop")
    print(trans)


if __name__ == '__main__':
    main()

