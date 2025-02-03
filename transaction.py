from budget import Budget
from datetime import datetime

class Transaction:
    def __init__(self, dollar_amount, budget_category, shop_website):
        self._dollar_amount     = self.__validate_dollar_amount(dollar_amount)
        self._budget_category   = self.__validate_budget_category(budget_category)
        self._shop_website = self.__validate_shop_website(shop_website)
        self._timestamp         = datetime.now()

    @staticmethod
    def __validate_dollar_amount(amount):
        """Prompt the user until they enter a positive number."""
        while True:
            if isinstance(amount, (int, float)) or amount > 0:
                return amount
            amount = float(input('Invalid dollar amount, please enter a valid dollar amount: '))

    @staticmethod
    def __validate_budget_category(category_index):
        """Prompt the user until they enter a valid budget category index."""
        while True:
            try:
                category_index = int(category_index)  # Convert input to integer
                if 0 <= category_index < len(Budget.BUDGET_TYPE):
                    return category_index
                else:
                    print(
                        f"Invalid category index: {category_index}. Must be between 0 and {len(Budget.BUDGET_TYPE) - 1}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer category index.")

            # Prompt user for correct input
            category_index = input(f"Enter a category index (0-{len(Budget.BUDGET_TYPE) - 1}): ")

    @staticmethod
    def __validate_shop_website(name):
        """Prompt the user until they enter a valid shop/website name."""
        while True:
            name = str(name).strip()  # Ensure input is a stripped string
            if name:
                return name
            print("Shop/website name must be a non-empty string.")
            name = input("Enter a valid shop/website name: ")

    def get_timestamp(self):
        return self._timestamp

    def get_dollar_amount(self):
        return self._dollar_amount

    def get_budget_category(self):
        return self._budget_category

    def get_budget_category_name(self):
        return Budget.get_budget_name(self._budget_category)

    def get_shop_website(self):
        return self._shop_website

    def __str__(self):
        """
        Format transaction details using ASCII art.
        """
        return (
            "+-------------------------------------------------------------+\n"
            f"| Category: {self.get_budget_category_name():<50}|\n"
            f"| Date and Time: {self.get_timestamp().strftime('%Y-%m-%d %H:%M'):<45}|\n"
            f"| Shop/Website: {self.get_shop_website():<46}|\n"
            f"| Amount Spent: ${self.get_dollar_amount():>10.2f}                                   |\n"
            "+-------------------------------------------------------------+"
        )
