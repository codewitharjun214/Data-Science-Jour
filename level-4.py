"""#1

marks = int(input("enter your marks :"))
status = "pass"
if marks >= 90 :
    print("you are in grade A",status)

elif marks >= 75 :
    print("you are in grade B",status)

elif marks >= 60 :
    print("you are in grade C",status)

elif marks >= 40 :
    print("you are in grade D",status)

else :
    print("you are fail")

#2 Atm Withdraw system
balance = int(input("enter your balance :"))
withdraw_money = int(input("enter the amount :"))
if withdraw_money > balance :
    print("withdraw money is greater than balance")
else :
    balance -= withdraw_money
    print("remaining balance :", balance)
    print("withdraw successful")

#3 Login System

username = (input("enter your username :"))
password = (input("enter your password :"))

if username >= '4' and password >= '8' :
    print("user is valid")
else:
    print("username is invalid")


#19 Movie Ticket Pricing System Ticket price based on age


age = int(input("enter your age :"))

if age <= 5 :
    print("your ticket price is free")

elif age <= 12 :
    print("your ticket price is 100")

elif age <= 60 :
    print("your ticket price is 200")

else :
    print("your ticket price is 120")

# 20 customer discount system

bill_amount = int(input("enter your bill amount: "))

if bill_amount > 100:
    discount = bill_amount * 10 / 100
    print("your discount is", discount)
else:
    print("no discount")"""

# 21 check number is  palindrome










