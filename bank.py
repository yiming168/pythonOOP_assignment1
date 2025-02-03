class Bank:
    def __init__(self, bank_account_number, bank_name, bank_balance):
        self._bank_account_number = self.__validate_account_number(bank_account_number)
        self._bank_name           = self.__validate_bank_name(bank_name)
        self._bank_balance        = self.__validate_balance(bank_balance)

    @staticmethod
    def __validate_account_number(account_number):
        """Keep asking for a valid account number until entered"""
        while True:
            if isinstance(account_number, str) and account_number.strip():
                return account_number.strip()
            account_number = input("Invalid account number. Please enter a non-empty string: ")

    @staticmethod
    def __validate_bank_name(name):
        """Keep asking for a valid bank name until entered"""
        while True:
            if isinstance(name, str) and name.strip():
                return name.strip()
            name = input("Invalid bank name. Please enter a non-empty string: ")

    @staticmethod
    def __validate_balance(balance):
        """Keep asking for a valid balance until entered"""
        while True:
            try:
                balance = float(balance)
                if balance >= 0:
                    return balance
            except ValueError:
                pass  # Ignore conversion errors
            balance = input("Invalid balance. Please enter a non-negative number: ")

    @property
    def account_number(self):
        return self._bank_account_number

    @property
    def name(self):
        return self._bank_name

    @property
    def balance(self):
        return self._bank_balance

    def deduct_balance(self, amount):
        """Safe balance deduction with validation"""
        try:
            amount = float(amount)
            if 0 < amount <= self._bank_balance:
                self._bank_balance -= amount
                return True
            print("Deduction amount invalid or exceeds balance")
            return False
        except (ValueError, TypeError):
            print("Invalid deduction amount format")
            return False

    def __str__(self):
        return (f"Bank Account Number: {self.account_number}, "
                f"Name: {self.name}, "
                f"Balance: {self.balance:.2f}")