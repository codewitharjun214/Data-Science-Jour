#Number Properties: For number 29, check if it's positive, even, and divisible by 3

num = 29

print("Is Positive:",num >= 1)
print("Is Even:",num % 2 == 0)
print("Is Divisible by 3:",num % 3 == 0)


#Leap Year Checker: Check if 2024 is a leap year (divisible by 4 and not by 100,
#unless also divisible by 400)

num = 2024

print("Is DIVIsible by 400:",num == 0)
print("Is Divisible By 4:",num % 4 == 0)
print("Is not Divisible by 100:",num % 3 != 0)

#Shipping Cost: Calculate cost: ₹50 base + ₹20/kg for weight>5kg, with 10%
#discount for online orders


weight = 8
is_online = True

ase_cost = 50
extra_cost = max(0, weight - 5) * 20
total_cost = base_cost + extra_cost

# Discount using boolean logic
discount = total_cost * 0.10 * is_online

# Final cost
final_cost = total_cost - discount

# Output
print("Weight:", weight, "kg")
print("Online Order:", is_online)
print("Shipping Cost: ₹", final_cost)

#Data Usage: Calculate remaining data from 10GB plan after using 2.3GB, 1.7GB,
#and 0.8GB

total_data = 10

use1 = 2.3
use2 = 1.7
use3 = 0.8

total =  use1 + use2 + use3
total_used = total_data - total
print("Total Used:", total_used)


#Password Strength: Check if password has ≥8 chars, contains digit, and has
#special char (!@#$)

password = input("Enter Password:")

length_check = len(password) >=8
digit_check = False
special_check = False

print("Password Length:", length_check)
print("Special Check:", special_check)
print("Digit Check:", digit_check)



