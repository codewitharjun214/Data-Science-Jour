# ✅ Q15
students = {
    "student1": {"name": "Rahul", "cgpa": 8.2},
    "student2": {"name": "Sneha", "cgpa": 9.1}
}

# Only Rahul's CGPA
print("Rahul CGPA:", students["student1"]["cgpa"])

# All student names
for key in students:
    print("Student Name:", students[key]["name"])


# ✅ Q16
print("List of Keys:", list(students.keys()))
print("List of Values:", list(students.values()))
print("List of Tuples:", list(students.items()))


# ✅ Q17 (Interview Level)

# 1️⃣ Duplicate Key
demo = {"a": 10, "a": 20}
print("Duplicate Key Result:", demo)
# Output: {'a': 20}
# Last value overwrites previous value

# 2️⃣ Mutable Type as Key (Not Allowed)

# This will give error:
# wrong = {[1,2]: "List Key"}   # TypeError: unhashable type: 'list'

# Because dictionary keys must be immutable (int, string, tuple)