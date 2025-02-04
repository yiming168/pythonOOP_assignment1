class User:
    def __init__(self, name, age):
        self._name = self.__validate_name(name)
        self._age  = self.__validate_age(age)

    @staticmethod
    def __validate_name(name):
        """Keep asking for a valid name until the user enters one."""
        while True:
            if isinstance(name, str) and name.strip():
                return name.strip()
            name = input("Please enter a non-empty name: ")

    @staticmethod
    def __validate_age(age):
        """Keep asking for a valid age until the user enters one."""
        while True:
            try:
                age = int(age)
                if age > 0:
                    return age
            except ValueError:
                pass  # Ignore invalid conversion errors
            age = input("Please enter a positive integer for age: ")

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __str__(self):
        return f"User Name: {self._name}, Age: {self._age}"
