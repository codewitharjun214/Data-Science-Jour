#1

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
    print("no discount")

# Write a program to check whether a number is a 3-digit number

num = int(input("Enter a number: "))

if (num >= 100 and num <= 999) or (num <= -100 and num >= -999):
    print("It is a 3-digit number")
else:
    print("It is not a 3-digit number")


# Write a program to check whether a number is palindrome.


text = input("Enter your data: ")


if text == text[::-1]:
    print("Palindrome ")
else:
    print("Not a palindrome ")


#Write a program to check whether a character is uppercase, lowercase, digit, or special symbol.

value = input("Enter a character: ")

if value >= 'A' and value <= 'Z':
    print("Uppercase letter")

elif value >= 'a' and value <= 'z':
    print("Lowercase letter")

elif value >= '0' and value <= '9':
    print("Digit")

else:
    print("Special symbol")


#Write a program to calculate bonus: Experience ≥ 5 years → 20% bonus Else → 10% bonus

salary = int(input("Enter your salary: "))
experience = int(input("Enter your experience in years: "))

if experience >= 5:
    bonus = salary * 20 / 100
else:
    bonus = salary * 10 / 100

print("Bonus amount is:", bonus)


#Write a program to determine password strength based on length.

password = input("Enter your password: ")

length = len(password)

if length < 6:
    print("Weak Password")
elif length < 10:
    print("Medium Password")
else:
    print("Strong Password")
























