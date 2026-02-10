#Quadratic Roots: Calculate roots of x² - 5x + 6 = 0 using formula: (-b ± √(b²-
#4ac))/(2a)



# Given equation: x^2 - 5x + 6 = 0

a = 1
b = -5
c = 6

# Calculate discriminant
d = b*b - 4*a*c

# Calculate roots using formula
root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)

print("Root 1:", root1)
print("Root 2:", root2)

#Number Reversal: Reverse digits of 12345 without string conversion
#problem 2

num = 12345

d1 = num % 10          # 5
num = num // 10        # 1234

d2 = num % 10          # 4
num = num // 10        # 123

d3 = num % 10          # 3
num = num // 10        # 12

d4 = num % 10          # 2
num = num // 10        # 1

d5 = num % 10          # 1

rev = d1*10000 + d2*1000 + d3*100 + d4*10 + d5

print("Reversed number:", rev)

#Prime Check: Check if 97 is prime using modulo operator

