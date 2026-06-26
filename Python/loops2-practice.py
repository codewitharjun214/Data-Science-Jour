
#  A. PATTERN PRINTING (Using Loops Only)

# =====================================================

# 1️⃣ Print a square pattern of * of size n

n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
print()

print("\n")

# 2️⃣ Print a square pattern using numbers from 1 to n in each row

n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end=" ")
print()

print("\n")

# 3️⃣ Print a square pattern where each row prints the same character

for i in range(5):
    print("A" * 5)

print("\n")

# 4️⃣ Print a right-angled triangle of stars

n = 6
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
print()

print("\n")

# 5️⃣ Print a triangle using numbers starting from 1 in each row

n = 6
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
print()

print("\n")

# 6️⃣ Print a triangle where each row contains only the row number

n = 4
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
print()

print("\n")

# 7️⃣ Print an inverted right-angled triangle

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
print()

print("\n")

# 8️⃣ Print a triangle of alternating 0s and 1s

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print("1", end=" ")
else:
    print("0", end=" ")
print()

print("\n")

# 9️⃣ Print a center-aligned pyramid of stars

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
for k in range(2 * i - 1):
    print("*", end="")
print()

print("\n")

# 🔟 Print a pyramid of numbers

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
for k in range(1, i + 1):
    print(k, end="")
for k in range(i - 1, 0, -1):
    print(k, end="")
print()

print("\n")

# 1️⃣1️⃣ Print a pyramid using alphabets

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
for k in range(i):
    print(chr(65 + k), end="")
for k in range(i - 2, -1, -1):
    print(chr(65 + k), end="")
print()

print("\n")

# 1️⃣2️⃣ Print a reverse pyramid

n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
for k in range(2 * i - 1):
    print("*", end="")
print()

print("\n")

# 1️⃣3️⃣ Print a full diamond of stars

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
for k in range(2 * i - 1):
    print("*", end="")
print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
for k in range(2 * i - 1):
    print("*", end="")
print()

print("\n")

# 1️⃣4️⃣ Print a diamond using numbers

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
for k in range(1, i + 1):
    print(k, end="")
for k in range(i - 1, 0, -1):
    print(k, end="")
print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
for k in range(1, i + 1):
    print(k, end="")
for k in range(i - 1, 0, -1):
    print(k, end="")
print()

print("\n")

# 1️⃣5️⃣ Print a hollow diamond

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
for k in range(1, 2 * i):
    if k == 1 or k == 2 * i - 1:
        print("*", end="")
else:
    print(" ", end="")
print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
for k in range(1, 2 * i):
    if k == 1 or k == 2 * i - 1:
        print("*", end="")
else:
    print(" ", end="")
print()

print("\n")

# 1️⃣6️⃣ Print a hollow square

n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
else:
    print(" ", end=" ")
print()

# =====================================================

# 🧠 B. LIST COMPREHENSION

# =====================================================

# 1️6 Even numbers (1–50)

evens = [x for x in range(1, 51) if x % 2 == 0]

# 17 Odd numbers (1–100)

odds = [x for x in range(1, 101) if x % 2 != 0]

# 18 Squares (1–20)

squares = [x * x for x in range(1, 21)]

# 19⃣ Replace negatives with 0

nums = [-5, 3, -1, 7]
result = [x if x >= 0 else 0 for x in nums]

# 20 Extract vowels

s = "programming"
vowels = [ch for ch in s if ch.lower() in "aeiou"]

# 21 Numbers divisible by 3 and 5

nums35 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]

# 22 Length of words

sentence = "Python is very powerful"
lengths = [len(word) for word in sentence.split()]

# 23 Convert string to uppercase

s = "python"
upper = [ch.upper() for ch in s]

# 24 Remove duplicates

nums = [1, 2, 2, 3, 4, 3, 5]
unique = []
for x in nums:
    if x not in unique:
        unique.append(x)

# 25 Prime numbers in range

primes = []
for num in range(1, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
else:
    primes.append(num)

# 🐢 C. TURTLE PROGRAMS


import turtle

t = turtle.Turtle()

# 26 Draw a square

for _ in range(4):
    t.forward(100)
t.right(90)
