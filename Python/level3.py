marks = int(input("enter your marks :"))
if marks >= 90 :
    print("you are in grade A")

elif marks >= 75 :
    print("you are in grade B")

elif marks >= 60 :
    print("you are in grade C")

elif marks >= 40 :
    print("you are in grade D")

else :
    print("you are fail")

#2
num1 = 10
num2 = 20
num3 = 30

if num1 > num2 and num1 > num3:
    print("Num1 is greater")

elif num2 > num1 and num2 > num3:
    print("Num2 is greater")

else :
    print("Num3 is greater")

#3

month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number")

#4
day =int(input("enter the day (1-7)"))
if day == 1 :
    print("Monday")
elif day == 2 :
    print("Tuesday")
elif day == 3 :
    print("Wednesday")
elif day == 4 :
    print("Thursday")
elif day == 5 :
    print("Friday")
elif day == 6 :
    print("Saturday")
elif day == 7 :
    print("Sunday")
else :
    print("Invalid day number")


#15
units = int(input("enter the number of units : "))

increase= (20 * units)

print(increase)

