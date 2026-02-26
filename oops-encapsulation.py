# Encapsulation means hiding internal data and allowing access only through methods.
# For this we have to use three concept to understand
# 1- Private variable
# 2 Get method - Get is used to display teh data
# Set method -set is used to setting the values and modification.

# private var is defined by _ (underscore)
#

#ex 1
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def set_balance(self, amount):
        if amount < 0:
            print("invalid amount")

        else:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account1 = Bank(10000)
print(account1.get_balance())
account1.set_balance(100)
print(account1.get_balance())

print("--------------------------------")
#Example 2
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
print(account.get_balance())