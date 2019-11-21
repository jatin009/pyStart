class InsufficientBalanceError(RuntimeError):
    pass


class BankAccount:
    def __init__(self, name, amount, account_number):
        self.customerName = name
        self.amount = amount
        self.account_number = account_number

    def deposit(self, amount):
        self.amount = self.amount + amount

    def withdraw(self, amount):
        if amount > self.amount:
            raise InsufficientBalanceError()
        self.amount = self.amount - amount
