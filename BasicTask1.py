#Practice Question 1
# 1. Temperature Conversion: Convert 98.6°F to Celsius using: C = (F - 32) × 5/9
a = 98.6
C = (a - 32 ) * 5/9
print(C)

#Practice Question 2
#Circle Calculations: Calculate area and circumference of a circle with radius 7.5
#cm

a = int(3.14*7.5**2)
print("Area of Circle",a)

a = int(2*3.14 * 7.5)
print("Area of Circum",a)


#Practice Question 3
#BMI Calculator: Calculate BMI for weight=68kg, height=1.75m (BMI =
#weight/height²)


weight = 68
height = 1.75
BMI = weight / (height*2)
print(BMI)

#Practice Question 4
#4. Time Converter: Convert 5678 seconds to hours, minutes, and remaining
#seconds

total_seconds = 5678

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

#Compound Interest: Calculate final amount for ₹5000 at 8% annual interest for 3
#years: A = P(1 + r/100)^t

P = 5000
r = 8
t = 3

A = P * (1 + r/100) ** t
print(f"Final Amount = ₹{A:.2f}")

