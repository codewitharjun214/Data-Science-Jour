import json
import random 
import string
from pathlib import Path



class Bank:
    def createaccount(self):
        pass

user = Bank()

print("press 1 for creating a new account")
print("press 2 for deposit the money in the bank")
print("press 3 for withdraw the money from the bank")
print("press 4 for the details of the account holder")
print("press 5 for the updating the details of the account holder")
print("press 6 for the deleting the account holder")

check = int(input("Enter your choice: "))

if check == 1:
    user.createaccount()

