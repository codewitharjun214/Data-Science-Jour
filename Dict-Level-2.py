# ✅ Q6
car = {"brand": "Toyota", "year": 2020}

car.update({"year": 2023, "color": "Black"})
print("Updated Car:", car)


# ✅ Q7
for key, value in car.items():
    print(key, ":", value)


# ✅ Q8
marks = {
    "Rahul": 85,
    "Sneha": 90,
    "Amit": 78
}

# Print all student names
print("Student Names:")
for name in marks.keys():
    print(name)

# Print all marks
print("Marks:")
for mark in marks.values():
    print(mark)

# Print name and mark together
print("Name and Marks:")
for name, mark in marks.items():
    print(name, ":", mark)


# ✅ Q9
student = {"name": "Riya", "cgpa": 9.2}

if "age" in student:
    print("Age exists")
else:
    print("Age does not exist")


# ✅ Q10
student.pop("cgpa")
print("After Removing CGPA:", student)