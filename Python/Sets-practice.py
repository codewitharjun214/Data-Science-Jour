# # """
# # Q1.Create a set:
# #
# # numbers = {10, 20, 30}
# #
# #
# # Add 40
# #
# # Try adding 20 again
# #
# # Print the result
# # 👉 What do you observe?
# # """

set = {10, 20, 30}

set.add(40)

print(set)

set.add(20)
print(set)


# # """
# # ✅ Q2.
# #
# # Create a set:
# #
# # colors = {"red", "blue"}
# #
# #
# # Use .update() to add:
# # "green"
# # "yellow"
# # "blue"
# # Print the result.
# # """

colours = {"red", "blue"}
colours.update({"green", "yellow","blue"})
print(colours)


# # """
# # ✅ Q3.
# #
# # Create a set:
# #
# # fruits = {"apple", "banana", "mango"}
# #
# #
# # Remove "banana" using .remove()
# # Print the set.
# # """
# # #
fruits = {"apple", "banana", "mango"}
fruits.remove("banana")
print(fruits)
# #
# # """
# # ✅ Q4.
# #
# # Create a set:
# #
# # marks = {45, 67, 89}
# #
# #
# # Try removing 100.
# # 👉 What error do you get?
# #
# # """
marks = {45, 67, 89}
marks.remove(100)
print(marks)


# # # #error i get is KeyError: 100
# #
# # """
# # 🔹 Level 2: Intermediate Practice
# # ✅ Q5.
# #
# # Take input from the user:
# #
# # Enter 5 numbers separated by space
# #
# #
# # Convert them into a set
# #
# # Add number 100
# #
# # Print final set
# # """

numbers = input("Enter 5 numbers separated by space: ")

# Convert string into list
numbers_list = numbers.split()

# Convert list into integers
numbers_list = [int(i) for i in numbers_list]

# Convert list into set
numbers_set = set(numbers_list)

# Add 100
numbers_set.add(100)

print("Final set:", numbers_set)


# # ✅ Q6.
# #
# # Given:
# #
# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}
# #
# #
# # Use .update() to merge set2 into set1
# #
# # Print set1

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print(set1)

set2.update(set1)
print(set2)

#
# Create a set of even numbers from 1–10.
# Then:
#
# Remove 4
#
# Add 12
#
# Print the final set

set = {1,2,3,4,5,6,7,8,9,10}

set.remove(4)
print(set)

set.add(12)
print(set)


# """# ✅ Q8.
# #
# # Given:
# #
# # data = {"Python", "Java", "C++"}
# #
# #
# # Remove "Java"
# #
# # Add "SQL"
# #
# # Add "Python" again
# #
# # Print the result
# #
# # 👉 Does it store duplicates? --- no
# """

data = {"Python", "Java", "C++"}

data.remove("Java")
data.add("SQL")
data.add("Python")

print(data)