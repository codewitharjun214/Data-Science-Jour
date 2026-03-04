#1
try:

   number1 = int(input("Enter a number: "))
   number2 = int(input("Enter another number: "))
   result = number1 / number2
   print(result)
except ZeroDivisionError:
    print("can not Divide by zero")
except ValueError:
    print("Value Error")
from logging import raiseExceptions

#2

try:
    number1 = int(input("Enter a number: "))

except Exception as e:
    print("please enter a valid number ",e)

#3

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index number: "))
    print("Element at index", index, "is", numbers[index])

except IndexError:
    print("Index out of range!")

except ValueError:
    print("Please enter a valid integer index.")

#4
try:
    number = 10
    string = "Hello"

    addition = number + string
except TypeError:
    print("TypeError : you are not allowed to add number and strings")

#5
try:
    number = float(input("Enter a number: "))
    number2 =float(input("Enter another number: "))
    divide = number / number2
    print("result:",divide)

except ZeroDivisionError:
    print("can not Divide by zero")

except ValueError:
    print("Value Error")

#Raise Practice
#6

try:
    age = int(input("Enter a number: "))
    if age < 0:
        raise ValueError("age can't be negative")
    print("age:",age)

except Exception as e:
    print("please enter a valid number ",e)

#7

try:
    marks = int(input("Enter a number: "))
    if marks <=0 or marks >100:
        raise ValueError("marks can't be less than 100")
    print("marks:",marks)

except Exception as e:
    print("please enter a valid marks ",e)

#8

try:
    password = input("Enter a password: ")
    if len(password) < 6:
        raise ValueError("password can't be less than 6")
    print("password:",password)

except Exception as e:
    print("please enter a valid password ",e)

#9
#using finally

try:
    number = int(input("Enter a number: "))
    divide = number / 100
    print("result:",divide)

finally:
    print("end of program")

#10

try:
    file = open("data.txt", "r")   # Open file in read mode
    content = file.read()          # Read content
    print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    print("File operation completed")

#11

while True:
    try:
        number = float(input("Enter a number: "))
        print("Valid number entered:", number)
        break   # Stop loop if input is valid

    except ValueError:
        print("Invalid input. Please enter a valid number.")

