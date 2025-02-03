
class Budget:

    BUDGET_TYPE = [
        "Games and Entertainment",
        "Clothing and Accessories",
        "Eating Out",
        "Miscellaneous"
    ]

    LIMIT, SPENT, STATUS = 0, 1, 2
    NUM_STAR = 50

    def __init__(self, *budgets_usd):
        self._budget_list =[]
        for i in range(len(Budget.BUDGET_TYPE)):
            if i < len(budgets_usd):
                self._budget_list.append([budgets_usd[i], 0, False])
            else:
                self._budget_list.append([0, 0, False])

    @classmethod
    def _validate_index(cls,index):
        if index < 0 or index > len(cls.BUDGET_TYPE):
            raise ValueError("Index out of range")

    @classmethod
    def get_budget_name(cls,index):
        cls._validate_index(index)
        return Budget.BUDGET_TYPE[index]

    @staticmethod
    def display_budget_choices():
        """Display budget categories and prompt the user to select one."""
        print("\nAvailable Budget Categories:")
        for i, category in enumerate(Budget.BUDGET_TYPE):
            print(f"  {i + 1}: {category}")  # Display index and category name

    def get_budget_list(self):
        return self._budget_list

    def get_limit(self, index):
        self._validate_index(index)
        return self._budget_list[index][Budget.LIMIT]

    def get_spent(self, index):
        self._validate_index(index)
        return self._budget_list[index][Budget.SPENT]

    def get_locked_status(self, index):
        self._validate_index(index)
        return self._budget_list[index][Budget.STATUS]

    def set_limit(self, index, limit):
        self._validate_index(index)
        if limit < 0:
            raise ValueError("Budget limit cannot be negative.")
        self._budget_list[index][Budget.LIMIT] = limit

    def set_spent(self, index, spent):
        self._validate_index(index)
        if spent < 0:
            raise ValueError("Amount spent cannot be negative.")
        self._budget_list[index][Budget.SPENT] = spent

    def set_budget_status(self, index, status):
        self._validate_index(index)
        self._budget_list[index][Budget.STATUS] = status

    def deduct_spent(self, index, amount):
        self._validate_index(index)
        if amount <= 0:
            raise ValueError("Amount to deduct must be positive.")
        self._budget_list[index][Budget.SPENT] += amount

    def get_locked_categories_num(self):
        result = 0
        for budget in self._budget_list:
            if budget[Budget.STATUS]:
                result += 1
        return result

    def get_remaining(self,index):
        self._validate_index(index)
        return self.get_limit(index) - self.get_spent(index)

    def get_total_remaining(self):
        result = 0
        for budget in self._budget_list:
            result += budget[Budget.LIMIT] - budget[Budget.SPENT]
        return result

    def get_budget_detail(self):
        """
        Generate a detailed ASCII-formatted string for all budgets.
        """
        detail_budget = "\n" + "=" * Budget.NUM_STAR + "\n"
        detail_budget += "||{:^46}||\n".format("Current Status of Budgets")
        detail_budget += "=" * Budget.NUM_STAR + "\n"

        for budget in self._budget_list:
            budget_name = Budget.BUDGET_TYPE[self._budget_list.index(budget)]
            budget_limit = budget[Budget.LIMIT]
            budget_spent = budget[Budget.SPENT]
            budget_remain = budget_limit - budget_spent
            budget_status = "Locked" if budget[Budget.STATUS] else "Unlocked"

            # Add budget details with ASCII formatting
            detail_budget += "-" * Budget.NUM_STAR + "\n"
            detail_budget += f"  Category: {budget_name}\n"
            detail_budget += f"  Limit:    ${budget_limit:.2f}\n"
            detail_budget += f"  Spent:    ${budget_spent:.2f}\n"
            detail_budget += f"  Left:     ${budget_remain:.2f}\n"
            detail_budget += f"  Status:   {budget_status}\n"
            detail_budget += "-" * Budget.NUM_STAR + "\n"

        return detail_budget
