# it is used to hide inner implementation

from abc import ABC, abstractmethod
class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

#polymorphism

class Ford(Car):

    def start(self):
        print("Ford Started")

    def stop(self):
        print("Ford Stopped")

#obj

c = Ford()
c.start()
c.stop()

print("-------------------------------")

#ex 2
from abc import ABC, abstractmethod

# Abstract Class
class BankAccount(ABC):

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("New Balance:", self.balance)


# Savings Account
class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn from Savings:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")


# Current Account
class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if amount <= self.balance + 5000:   # Overdraft allowed
            self.balance -= amount
            print("Withdrawn from Current:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Overdraft Limit Exceeded")


# Creating Objects
s = SavingsAccount("S123", 10000)
c = CurrentAccount("C456", 5000)

s.deposit(2000)
s.withdraw(5000)

print("-----")

c.withdraw(8000)
