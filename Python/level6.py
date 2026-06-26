#Write a program to calculate income tax based on salary slabs.
#26


salary = int(input("Enter your annual salary: "))
tax = 0

if salary <= 250000:
    tax = 0

elif salary <= 500000:
    tax = (salary - 250000) * 0.05

elif salary <= 1000000:
    tax = (250000 * 0.05) + (salary - 500000) * 0.20

else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (salary - 1000000) * 0.30

print("Income Tax =", tax)


#Write a program to check whether three sides form a valid triangle.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


#Write a program to determine BMI category

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print("BMI =", bmi)

if bmi < 18.5:
    print("Category: Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Category: Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

#Write a program to check eligibility for loan based on salary and credit score.
salary = int(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score: "))

if salary >= 25000 and credit_score >= 700:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")


#Write a program to build a traffic light system.

signal = input("Enter traffic light color (red/yellow/green): ")

if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("READY")
elif signal == "green":
    print("GO")
else:
    print("Invalid signal")

