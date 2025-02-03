from typing import List

from user import User
from budget import Budget
from transaction import Transaction
from bank import Bank
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, user_name, age,
                 bank_name, account_num, balance,
                 *budgets_usd):
        self._user = User(user_name, age)
        self._bank = Bank(bank_name, account_num, balance)
        self._budget = self.__validate_budgets(Budget(*budgets_usd), self._bank)
        self._transactions: List[Transaction] = []
        self._locked_status = False

    @staticmethod
    def __validate_budgets(origin_budgets: Budget, bank: Bank) -> Budget:
        """Ensure budgets are non-negative and do not exceed the bank balance."""

        while True:
            total_budget = origin_budgets.get_total_budget_remaining()

            # Check for negative budgets
            if any(b[Budget.LIMIT] < 0 for b in origin_budgets.get_budget_list()):
                print("Error: Individual budgets cannot be negative.")
            # Check if total budget exceeds balance
            elif total_budget > bank.balance:
                print(f"Error: Total budget (${total_budget:.2f}) cannot exceed bank balance (${bank.balance:.2f}).")
            else:
                return origin_budgets # Valid budgets

            # Prompt user to re-enter valid budgets
            print("Please re-enter budgets for each category:")
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

    @abstractmethod
    def send_exceed_limit_message(self, selection):
        pass

    def view_budgets(self):
        print(self.get_budget().get_budget_detail())

    def get_user(self):
        return self._user

    def get_bank(self):
        return self._bank

    def get_budget(self):
        return self._budget

    def get_transaction(self):
        return self._transactions

    def get_locked_status(self):
        return self._locked_status