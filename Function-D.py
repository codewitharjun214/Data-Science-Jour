# ✅ Q13 - Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# ✅ Q14 - Sum of First N Natural Numbers
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print("Sum of N:", sum_n(5))


# ✅ Q15 - Power Function
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print("Power:", power(2, 3))


# ✅ Q16 - Print Numbers from N to 1
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)

print_numbers(5)


# ✅ Q17 - Fibonacci Series
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci:", fibonacci(6))