'''
A static method belongs to the class, not an object.

It doesn’t use self or cls, so it cannot access instance or class variables directly.

Often used for utility functions that relate to the class but don’t need an object.
'''

class Bank:
    bank_name = "SafeBank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited {amount}. Balance: {self.balance}")

    @staticmethod
    def validate_amount(amount):
        """Check if the amount is valid (positive number)"""
        return amount > 0


# Check amount without creating a Bank account
print(Bank.validate_amount(100))  # True
print(Bank.validate_amount(-50))  # False

# Create an account and deposit
acc = Bank("Alice", 500)
if Bank.validate_amount(200):  # static method used here
    acc.deposit(200) # Alice deposited 200. Balance: 700


'''
validate_amount is logically part of Bank → it makes sense to keep it in the class.

You don’t need to create an account object just to validate an amount.

Keeps all Bank-related logic in one place → easy to maintain.
'''