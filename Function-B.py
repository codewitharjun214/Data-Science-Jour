# ✅ Q6
def add_numbers(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", add_numbers(num1, num2))


# ✅ Q7
def average(a, b, c):
    return (a + b + c) / 3

print("Average:", average(10, 20, 30))


# ✅ Q8
def max_number(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum:", max_number(15, 25))


# ✅ Q9
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number is:", check_even_odd(7))


# ✅ Q10
def total_sum(numbers):
    return sum(numbers)

nums = [10, 20, 30, 40]
print("Total Sum:", total_sum(nums))