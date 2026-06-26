# ✅ Q1
employee = {
    "name": "Arjun",
    "age": 21,
    "salary": 50000
}

print("Salary:", employee["salary"])

# for practice ...................

print("Keys:", employee.keys())
print("Values:", employee.values())
employee["salary"] = 90000
print("Salary:", employee["salary"])

#.................................

# ✅ Q2
student = {"name": "Amit", "age": 21, "cgpa": 7.8}

student["cgpa"] = 8.4
print("Updated CGPA:", student)

# for practice ...................

student.update(cgpa=9.4)
print(" second Updated CGPA:", student)


# ......................................


# ✅ Q3
student["branch"] = "IT"
print("After Adding Branch:", student)


# ✅ Q4
print("Keys:", student.keys())


# ✅ Q5
print("Values:", student.values())