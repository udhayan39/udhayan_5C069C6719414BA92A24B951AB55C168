class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Create an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
account.display_balance()  # Display initial balance
account.deposit(500.0)    # Deposit $500
account.withdraw(200.0)   # Withdraw $200
account.withdraw(1500.0)  # Try to withdraw an invalid amount
account.display_balance()  # Display updated balance
