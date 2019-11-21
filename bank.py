from bank_account import BankAccount
from bank_account import InsufficientBalanceError


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def __len__(self):
        return len(self.accounts)

    def add_account(self, customer_name, amount):
        account_no = int("1178015010{:02}".format(len(self)+1))
        acc = BankAccount(customer_name, amount, account_no)
        self.accounts.append(acc)
        return account_no

    def search_account(self, ac_no):
        for account in self.accounts:
            if account.account_number == ac_no:
                return account
        else:
            return None

    def query_portal(self):
        print(f"Welcome to {self.name} !")
        option = ""

        while option != 'quit':
            option = input("\nEnter 'add' if you are new or 'existing' for other options or 'quit' to exit: ")
            if option == 'add':
                name = input("Your name: ")
                try:
                    amt = int(input("Opening Balance: "))
                except ValueError:
                    print("Please input positive integer for opening balance.")
                    continue
                ac_no = self.add_account(name, amt)
                print(f"Account successfully added ! Your account number: {ac_no}")

            elif option == 'existing':
                try:
                    account_no = int(input("Enter your account number: "))
                except ValueError:
                    print("Please input valid account number.")
                    continue
                success = self.search_account(account_no)   # getting bank_account object in success

                choice = ""
                if not isinstance(success, BankAccount):        # In case it returns None
                    print("Sorry ! Your account number does not exist.")
                else:
                    while choice != 'exit':
                        choice = input(f"\nHi {success.customerName}, you would like to 'view', 'deposit' or "
                                       f"'withdraw' the amount or 'exit': ")
                        if choice == 'view':
                            print(f"Your main account balance is {success.amount}.")
                        elif choice == 'deposit':
                            try:
                                dep_amt = int(input("Enter the amount: "))
                            except ValueError:
                                print("Please enter positive integer.")
                                continue
                            success.deposit(dep_amt)
                            print(f"Your main account balance is {success.amount}.")
                        elif choice == 'withdraw':
                            try:
                                with_amt = int(input("Enter the amount: "))
                                success.withdraw(with_amt)
                            except ValueError:
                                print("Please enter positive integer.")
                                continue
                            except InsufficientBalanceError:
                                print("The requested amount exceeds the current balance in the account.")
                                continue
                            print(f"Your main account balance is {success.amount}.")

    def __repr__(self):
        print(f'<Bank {self.name} with {self.accounts}>')
