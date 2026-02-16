# SECTION 1 – Basic For Loop Practice

#print "Hello" 50 times using a for loop.

for i in range(1,51):
    print("hello",i)


# Print numbers from 1 to 20.

for i in range(1,21):
    print(i)

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Print all odd numbers between 1 and 30.

for i in range(1, 31):
    if i % 2 == 1:
        print(i)

# Print multiplication table of 7.

for i in range(1, 71):
    if i % 7 == 0:
        print(i)



# SECTION 2 – Basic While Loop
#  Print numbers from 10 to 1 using while


i = 10

while i >= 1:
    print(i)
    i = i - 1



#  Print sum of first 10 natural numbers.

i = 10
while i > 1:
    i = i - 1
    print(i)

# Print all multiples of 5 less than 100.

i = 5

while i < 100:
    print(i)
    i = i + 5



# Count how many numbers between 1 and 50 are divisible by 3.


i = 1
count = 0

while i <= 50:
    if i % 3 == 0:
        count += 1
    i += 1

print("Total numbers divisible by 3:", count)



# Keep taking input from user until they enter 0.

num = int(input("Enter number: "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter number: "))

print("Loop stopped because you entered 0")



# SECTION 3 – break Practice

#Print numbers from 1 to 100 but stop when number reaches 25.

for i in range(1, 101):
    if i == 25:
        break
    print(i)



# Ask user for password. Stop loop when correct password is entered.


# Ask user for password. Stop loop when correct password is entered.


password = "arjun"

enter = input("Enter password: ")

while enter != password:
    print("Wrong password. Try again.")
    enter = input("Enter password: ")

print("Correct password! Access granted.")


#Find first number divisible by both 4 and 6 between 1 and 100.

for i in range(1, 101):
    if i % 4 == 0 and i % 6 == 0:
        print("First number is:", i)
        break


#  Generate numbers from 1 to 100 and stop at first prime number.
for num in range(1, 101):

    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print("First prime number is:", num)
            break

# ================================
# SECTION 4 – continue Practice
# ================================

# 15️⃣ Print numbers from 1 to 20 but skip multiples of 3.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


# 16️⃣ Print numbers from 1 to 50 but skip even numbers.
for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i)


# 17️⃣ Print characters of a string but skip vowels.
text = "arjun"
for ch in text:
    if ch.lower() in "aeiou":
        continue
    print(ch)


# 18️⃣ Print numbers from 1 to 100 but skip numbers divisible by both 2 and 5.
for i in range(1, 101):
    if i % 2 == 0 and i % 5 == 0:
        continue
    print(i)


# ================================
# SECTION 5 – pass Practice
# ================================

# 19️⃣ Print numbers 1 to 10 but use pass inside loop.
for i in range(1, 11):
    pass
    print(i)


# 20️⃣ Function with loop body using pass.
def sample_function():
    for i in range(5):
        pass


# 21️⃣ Menu-driven program skeleton using pass.
while True:
    print("1. Option A")
    print("2. Option B")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        break
    else:
        print("Invalid choice")


# ================================
# SECTION 6 – Logic Based Loop Questions
# ================================

# 22️⃣ Factorial of a number using for loop.
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)


# 23️⃣ Reverse a number using while.
num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed:", rev)


# 24️⃣ Check if number is palindrome.
num = 121
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# 25️⃣ Count number of digits.
num = 12345
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digit count:", count)


# 26️⃣ Fibonacci series up to 10 terms.
a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b


# 27️⃣ Find largest number in a list.
numbers = [10, 45, 23, 89, 67]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)


# ================================
# SECTION 7 – Tricky Questions
# ================================

# 28️⃣ Output:
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0 1 2


# 29️⃣ Output:
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0 1 2 4


# 30️⃣ Output:
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Done")
# Output: 0 1 2 3 4 Done


# ================================
# BONUS
# ================================

# 31️⃣ Pattern
for i in range(1, 6):
    print(str(i) * i)


# 32️⃣ Prime numbers between 1 and 100.
for num in range(1, 101):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
