# ✅ Q11
def calculate(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul

result = calculate(10, 5)
print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])


# ✅ Q12
def square_cube(n):
    return n*n, n*n*n

sq, cube = square_cube(3)
print("Square:", sq)
print("Cube:", cube)