from user import User
from budget import Budget
from transaction import Transaction
from bank import Bank
from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, user_name, age,
                bank_name, account_num, balance,
                *budgets_usd):
        self._user          = User(user_name, age)
        self._bank          = Bank(bank_name, account_num, balance)
        self._budgets       = self.__validate_budgets(Budget(*budgets_usd), self._bank)
        self._transactions  = []
        self._locked_status = False


    @staticmethod
    def __validate_budgets(origin_budgets: Budget, bank: Bank) -> Budget:
        """Ensure budgets are non-negative and do not exceed the bank balance."""

        while True:
            total_budget = origin_budgets.get_total_remaining()

            # Check for negative budgets
            if any(b[Budget.LIMIT] < 0 for b in origin_budgets.get_budget_list()):
                pass
            # Check if total budget exceeds balance
            elif total_budget > bank.balance:
                print(f"Error: Total budget (${total_budget:.2f}) cannot exceed bank balance (${bank.balance:.2f}).")
            else:
                return origin_budgets # Valid budgets

            # Prompt user to re-enter valid budgets
            print("Please enter valid budgets for each category:")
            new_budgets = []
            for category in Budget.BUDGET_TYPE:
                while True:
                    try:
                        budget = float(input(f"Enter budget for {category}: "))
                        if budget < 0:
                            print("Budget cannot be negative. Try again.")
                            continue
                        new_budgets.append(budget)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

            # Create a new Budget instance with valid budgets
            origin_budgets = Budget(*new_budgets)

    @property
    @abstractmethod
    def user_type(self):
        pass

    @property
    @abstractmethod
    def notification_percent(self):
        pass

    @property
    @abstractmethod
    def locked_out_percent(self):
        pass

    @property
    @abstractmethod
    def locked_out_category_num(self):
        pass

    @abstractmethod
    def send_close_limit_message(self, selection):
        pass

    @property
    def user_name(self):
        return self._user.name

    @property
    def locked_status(self):
        return self._locked_status

    @property
    def transactions(self):
        return self._transactions


    def record_transaction(self):
        budget_category = self.__validate_category()
        dollar_amount   = self.__validate_dollar_amount()
        shop_website    = self.__validate_website()
        self.__update_account(budget_category, dollar_amount)
        self._transactions.append(Transaction(dollar_amount, budget_category, shop_website))
        self.handle_notification(budget_category)
        if self._budgets.get_locked_categories_num() >= self.locked_out_category_num:
            self._locked_status = True
        print("Transactions recorded")

    def view_budgets(self):
        print(self.get_budget().get_budget_detail())

    def get_budget_list(self):
        return self._budgets.BUDGET_TYPE

    def get_budget(self):
        return self._budgets

    def get_transaction(self):
        return self._transactions

    def view_transaction_by_budget(self, selection):
        budget_category_name = Budget.get_budget_name(selection -1)

        print(f"\nTransactions for {budget_category_name} category:")
        if not self.transactions[selection - 1]:
            print(f"No transaction recorded under the budget category {budget_category_name}.")
            return
        for transaction in self._transactions:
            if transaction.get_budget_category() == selection - 1:
                print(transaction)

    def __validate_category(self):
        """Ensure the budget category index is valid."""
        Budget.display_budget_choices()
        budget_category = input(f"Enter budget category index between 1 and {len(self._budgets.BUDGET_TYPE)}.")
        while True:
            try:
                index = int(budget_category) - 1
                if 0 <= index < len(Budget.BUDGET_TYPE) and not self._budgets.get_locked_status(index):
                    return index
                elif self._budgets.get_locked_status(index):
                    print(f"Locked category. Enter another number between 1 and {len(self._budgets.BUDGET_TYPE)}.")
                else:
                    print(f"Invalid selection. Enter a number between 1 and {len(self._budgets.BUDGET_TYPE)}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
            budget_category = input("Re-enter budget category index: ")

    def __validate_dollar_amount(self):
        """Ensure the dollar amount is a positive number"""
        dollar_amount = input("Enter dollar amount: ")
        while True:
            try:
                amount = float(dollar_amount)
                if 0 < amount <= self._bank.balance:
                    return amount
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
            dollar_amount = input("Invalid input. Enter a correct dollar amount: ")

    @staticmethod
    def __validate_website():
        """Ensure the shop/website name is a non-empty string, or allow cancellation."""
        shop_website = input("Re-enter shop name or website: ")
        while True:
            name = str(shop_website).strip()
            if name:
                return name
            print("Shop/website name cannot be empty.")
            shop_website = input("Re-enter shop name or website: ")

    def __update_account(self, category, amount):
        self._budgets.set_spent(category, amount)
        if self._budgets.get_spent(category) > self._budgets.get_limit(category) * self.locked_out_percent:
            self._budgets.set_budget_status(category, True)
        self._bank.deduct_balance(amount)

    def handle_notification(self,index):
        if self._budgets.get_spent(index) > self._budgets.get_limit(index) * self.notification_percent:
            self.send_close_limit_message(index)
        if self._budgets.get_spent(index) > self._budgets.get_limit(index) * self.locked_out_percent:
            self._budgets.set_budget_status(index, True)
            print("Current category has reached its limit, locked.")

    def get_detail(self):
        return (
            "===========================================\n"
            "||           Account Information         ||\n"
            "===========================================\n"
            f"  User Name:           {self._user.name}\n"
            f"  Age:                 {self._user.age}\n"
            f"  Bank Account Number: {self._bank.account_number}\n"
            f"  Bank Name:           {self._bank.name}\n"
            f"  Bank Balance:        ${self._bank.balance:,.2f}\n"
            f"  User Type:           {self.user_type}\n"
            f"  Account Lock Status: {'Locked' if self._locked_status else 'Unlocked'}\n"
            "===========================================\n"
        )

    def __str__(self):
        return f"User Name: {self._user.name}, Age: {self._user.age}, " \
               f"Bank Account Number: {self._bank.account_number}, " \
               f"Bank Name: {self._bank.name}, " \
               f"Bank Balance: {self._bank.balance}, " \
               f"User Type: {self.user_type}, " \
               f"Account Lock Status: {self._locked_status}"


