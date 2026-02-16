# ============================================
#        PYTHON LIST COMPLETE DOCUMENT
#        (Level 1 to Level 6)
# ============================================


# ============================================
# LEVEL 1: BASIC LIST CREATION
# ============================================

# 1️⃣ List is a collection of elements stored inside []
# Index starts from 0

nums = [10, 20, 30, 40, 50]
print(nums)        # Output: [10, 20, 30, 40, 50]


# 2️⃣ List can store multiple data types

data = [10, 5.5, "Arjun"]
print(data)        # Output: [10, 5.5, 'Arjun']


# 3️⃣ Empty list + append()
# append() adds one element at the end

items = []
items.append("Apple")
items.append("Banana")
items.append("Mango")
print(items)       # Output: ['Apple', 'Banana', 'Mango']


# 4️⃣ Indexing (starts from 0)

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print(fruits[2])   # Output: Mango


# 5️⃣ Negative Indexing
# -1 means last element

nums = [10, 20, 30, 40]
print(nums[-1])    # Output: 40



# ============================================
# LEVEL 2: INDEXING & SLICING
# ============================================

# Slicing format: list[start:end:step]

nums = [10, 20, 30, 40, 50, 60]

print(nums[1:5])    # Output: [20, 30, 40, 50]
print(nums[::2])    # Output: [10, 30, 50]
print(nums[::-1])   # Output: [60, 50, 40, 30, 20, 10]

print(nums[:3])     # Output: [10, 20, 30]
print(nums[-2:])    # Output: [50, 60]


# Check if element exists using 'in'

if 20 in nums:
    print("Exists")      # Output: Exists
else:
    print("Not Exists")



# ============================================
# LEVEL 3: LIST METHODS
# ============================================

# append() → add one item

grocery = []
grocery.append("Rice")
grocery.append("Milk")
grocery.append("Sugar")
print(grocery)
# Output: ['Rice', 'Milk', 'Sugar']


# extend() → add multiple items

grocery.extend(["Tea", "Salt"])
print(grocery)
# Output: ['Rice', 'Milk', 'Sugar', 'Tea', 'Salt']


# insert(index, value)

grocery.insert(2, "Oil")
print(grocery)
# Output: ['Rice', 'Milk', 'Oil', 'Sugar', 'Tea', 'Salt']


# remove(value) → removes specific item

grocery.remove("Milk")
print(grocery)
# Output: ['Rice', 'Oil', 'Sugar', 'Tea', 'Salt']


# pop() → removes last item

grocery.pop()
print(grocery)
# Output: ['Rice', 'Oil', 'Sugar', 'Tea']


# clear() → removes all items

grocery.clear()
print(grocery)
# Output: []


# count(value)

nums = [1, 5, 3, 5, 7, 5]
print(nums.count(5))
# Output: 3


# index(value)

fruits = ["Mango", "Apple", "Banana"]
print(fruits.index("Apple"))
# Output: 1


# sort() → ascending order

nums = [50, 10, 40, 20]
nums.sort()
print(nums)
# Output: [10, 20, 40, 50]


# reverse() → reverse order

nums.reverse()
print(nums)
# Output: [50, 40, 20, 10]



# ============================================
# LEVEL 4: LOGIC BASED PROGRAMS
# ============================================

nums = [10, 25, 5, 80, 30]

# Largest element

largest = nums[0]
for num in nums:
    if num > largest:
        largest = num

print("Largest:", largest)
# Output: Largest: 80


# Smallest element

smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)
# Output: Smallest: 5


# Sum of elements

total = 0
for num in nums:
    total += num

print("Sum:", total)
# Output: Sum: 150


# Count even and odd numbers

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
# Output:
# Even: 3
# Odd: 2


# Remove duplicates

nums = [1, 2, 2, 3, 4, 4, 5]
unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print(unique)
# Output: [1, 2, 3, 4, 5]


# Merge two lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2
print(merged)
# Output: [1, 2, 3, 4, 5, 6]



# ============================================
# LEVEL 5: INTERMEDIATE
# ============================================

# Replace second element

nums = [10, 20, 30]
nums[1] = 100
print(nums)
# Output: [10, 100, 30]


# Swap first and last

nums = [10, 20, 30]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)
# Output: [30, 20, 10]


# Second largest number

nums = [10, 20, 40, 30]
nums.sort()
print(nums[-2])
# Output: 30


# Palindrome list check

nums = [1, 2, 3, 2, 1]

if nums == nums[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
# Output: Palindrome



# ============================================
# LEVEL 6: MINI PRACTICAL PROGRAMS
# ============================================

# Grocery System

grocery = []
grocery.append("Rice")
grocery.append("Milk")
grocery.append("Sugar")
grocery.remove("Milk")

print("Items:", grocery)
print("Total:", len(grocery))
# Output:
# Items: ['Rice', 'Sugar']
# Total: 2


# Student Marks System

marks = [75, 80, 65, 90, 85]

average = sum(marks) / len(marks)

print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))
# Output:
# Average: 79.0
# Highest: 90
# Lowest: 65


# Shopping Cart

prices = []
prices.append(100)
prices.append(200)
prices.append(300)

print("Total:", sum(prices))
prices.pop()
print("After remove:", prices)
# Output:
# Total: 600
# After remove: [100, 200]



# ============================================
# END OF DOCUMENT
# ============================================

# List is:
# ✔ Ordered
# ✔ Mutable (changeable)
# ✔ Allows duplicates
# ✔ Supports slicing
# ✔ Supports many built-in methods
