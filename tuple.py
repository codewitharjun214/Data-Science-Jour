# ============================================
#        PYTHON TUPLE COMPLETE DOCUMENT
#        (Level 1 to Level 8)
# ============================================


# ============================================
# 🟢 LEVEL 1: BASIC TUPLE CREATION
# ============================================

# 1️⃣ Tuple is an ordered collection stored inside ()
# Tuple is immutable (cannot be changed)

t = (10, 20, 30, 40, 50)
print(t)
# Output: (10, 20, 30, 40, 50)


# 2️⃣ Tuple with mixed data types

t = (10, 5.5, "Arjun")
print(t)
# Output: (10, 5.5, 'Arjun')


# 3️⃣ Single element tuple
# Must use comma after element

t = (5,)
print(type(t))
# Output: <class 'tuple'>


# 4️⃣ Why is this not a tuple?

t = (5)
print(type(t))
# Output: <class 'int'>

# Because (5) is treated as an integer.
# Comma is required to create a single-element tuple.


# 5️⃣ Tuple without parentheses

t = 10, 20, 30
print(t)
# Output: (10, 20, 30)



# ============================================
# 🟡 LEVEL 2: INDEXING & SLICING
# ============================================

t = (10, 20, 30, 40, 50, 60)

# 6️⃣ First element
print(t[0])
# Output: 10


# 7️⃣ Last element
print(t[-1])
# Output: 60


# 8️⃣ Extract index 1 to 4
print(t[1:5])
# Output: (20, 30, 40, 50)


# 9️⃣ Last 3 elements
print(t[-3:])
# Output: (40, 50, 60)


# 🔟 Reverse tuple
print(t[::-1])
# Output: (60, 50, 40, 30, 20, 10)


# 1️⃣1️⃣ Every second element
print(t[::2])
# Output: (10, 30, 50)



# ============================================
# 🟠 LEVEL 3: TUPLE METHODS
# ============================================

t = (1, 2, 3, 2, 4, 2)

# 1️⃣2️⃣ count()
print(t.count(2))
# Output: 3


# 1️⃣3️⃣ index()
print(t.index(4))
# Output: 4


# 1️⃣4️⃣ Searching non-existing element

# print(t.index(10))
# Output: ValueError
# If element not found, Python raises ValueError.



# ============================================
# 🔵 LEVEL 4: LOGIC BASED PROGRAMS
# ============================================

t = (10, 25, 5, 80, 30)

# 1️⃣5️⃣ Maximum value
print(max(t))
# Output: 80


# 1️⃣6️⃣ Minimum value
print(min(t))
# Output: 5


# 1️⃣7️⃣ Sum of elements
print(sum(t))
# Output: 150


# 1️⃣8️⃣ Check existence

if 25 in t:
    print("Exists")
else:
    print("Not Exists")
# Output: Exists


# 1️⃣9️⃣ Convert tuple to list

lst = list(t)
print(lst)
# Output: [10, 25, 5, 80, 30]


# 2️⃣0️⃣ Convert list to tuple

lst = [1, 2, 3]
t = tuple(lst)
print(t)
# Output: (1, 2, 3)



# ============================================
# 🟣 LEVEL 5: NESTED TUPLES
# ============================================

t = ((1, 2), (3, 4), (5, 6))

# 2️⃣1️⃣ Access element 4
print(t[1][1])
# Output: 4


# 2️⃣2️⃣ Access element 6
print(t[2][1])
# Output: 6


# 2️⃣3️⃣ Second inner tuple
print(t[1])
# Output: (3, 4)


# 2️⃣4️⃣ Sum of all elements

total = 0
for inner in t:
    for num in inner:
        total += num

print(total)
# Output: 21



# ============================================
# 🔴 LEVEL 6: ADVANCED PRACTICE
# ============================================

# 2️⃣5️⃣ Sorted student names

students = ("Rahul", "Arjun", "Sita", "Aman")
print(tuple(sorted(students)))
# Output: ('Aman', 'Arjun', 'Rahul', 'Sita')


# 2️⃣6️⃣ Palindrome tuple

t = (1, 2, 3, 2, 1)

if t == t[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
# Output: Palindrome


# 2️⃣7️⃣ Swap two tuples

t1 = (1, 2)
t2 = (3, 4)

t1, t2 = t2, t1
print(t1, t2)
# Output: (3, 4) (1, 2)


# 2️⃣8️⃣ Unpacking tuple

t = (10, 20, 30)
a, b, c = t
print(a, b, c)
# Output: 10 20 30


# 2️⃣9️⃣ Unpacking more values than variables

# t = (10, 20, 30)
# a, b = t
# Output: ValueError (too many values to unpack)



# ============================================
# ⚫ LEVEL 7: PRACTICAL MINI TASKS
# ============================================

# 3️⃣0️⃣ Latitude and Longitude

location = (18.5204, 73.8567)
print("Latitude:", location[0])
print("Longitude:", location[1])


# 3️⃣1️⃣ Average of 5 numbers

nums = (10, 20, 30, 40, 50)
average = sum(nums) / len(nums)
print("Average:", average)
# Output: 30.0


# 3️⃣2️⃣ Employee records (ID, Name, Salary)

employees = (
    (1, "Arjun", 25000),
    (2, "Rahul", 30000),
    (3, "Sita", 28000)
)

print(employees)


# 3️⃣3️⃣ Extract second elements

t = ((1,10),(2,20),(3,30))

second_elements = ()

for pair in t:
    second_elements += (pair[1],)

print(second_elements)
# Output: (10, 20, 30)


# 3️⃣4️⃣ Remove duplicates

t = (1, 2, 2, 3, 4, 4, 5)
unique = tuple(set(t))
print(unique)
# Output: (order may vary)


# 3️⃣5️⃣ Even numbers from 1 to 20

even = tuple(i for i in range(1, 21) if i % 2 == 0)
print(even)
# Output: (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)



# ============================================
# 🧠 LEVEL 8: INTERVIEW QUESTIONS
# ============================================

# 3️⃣6️⃣ Why are tuples immutable?
# Tuples are immutable to make them:
# - Faster
# - Memory efficient
# - Safe for fixed data


# 3️⃣7️⃣ Why tuples can be dictionary keys?
# Dictionary keys must be immutable.
# Tuple is immutable, so it can be a key.
# List is mutable, so it cannot be a key.


# 3️⃣8️⃣ Which is faster?
# Tuple is faster than list because:
# - Immutable
# - Less memory usage


# 3️⃣9️⃣ Can tuple contain list?
# Yes.

t = (1, [2, 3], 4)
print(t)
# Output: (1, [2, 3], 4)


# 4️⃣0️⃣ Can list inside tuple be modified?
# Yes, because list itself is mutable.

t = (1, [2, 3], 4)
t[1][0] = 100
print(t)
# Output: (1, [100, 3], 4)



# ============================================
# END OF DOCUMENT
# ============================================

# Tuple Properties:
# ✔ Ordered
# ✔ Immutable
# ✔ Allows duplicates
# ✔ Supports indexing and slicing
# ✔ Only two built-in methods: count() and index()
