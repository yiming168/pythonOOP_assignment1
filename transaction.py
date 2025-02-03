from budget import Budget
from datetime import datetime

class Transaction:
    def __init__(self, dollar_amount, budget_category, shop_website_name):
        self._timestamp = datetime.now()
        self._dollar_amount = self.__validate_dollar_amount(dollar_amount)
        self._budget_category = self.__validate_budget_category(budget_category)
        self._shop_website_name = self.__validate_shop_website_name(shop_website_name)

    @staticmethod
    def __validate_dollar_amount(amount):
        """Validate that the dollar amount is a positive number."""
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Dollar amount must be a positive number.")
        return amount

    @staticmethod
    def __validate_budget_category(category_index):
        """Validate that the budget category index is within bounds."""
        if not isinstance(category_index, int) or category_index < 0 or category_index >= len(Budget.BUDGET_TYPE):
            raise ValueError(f"Invalid budget category index: {category_index}. Must be between 0 and {len(Budget.BUDGET_TYPE) - 1}.")
        return category_index

    @staticmethod
    def __validate_shop_website_name(name):
        """Validate that the shop/website name is a non-empty string."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Shop/website name must be a non-empty string.")
        return name.strip()

    def get_timestamp(self):
        return self._timestamp

    def get_dollar_amount(self):
        return self._dollar_amount

    def get_budget_category(self):
        return self._budget_category

    def get_budget_category_name(self):
        return Budget.get_budget_name(self._budget_category)

    def get_shop_website_name(self):
        return self._shop_website_name

    def __str__(self):
        """
        Format transaction details using ASCII art.
        """
        return (
            "+-------------------------------------------------------------+\n"
            f"| Category: {self.get_budget_category_name():<50}|\n"
            f"| Date and Time: {self.get_timestamp().strftime('%Y-%m-%d %H:%M'):<45}|\n"
            f"| Shop/Website: {self.get_shop_website_name():<46}|\n"
            f"| Amount Spent: ${self.get_dollar_amount():>10.2f}                                   |\n"
            "+-------------------------------------------------------------+"
        )
