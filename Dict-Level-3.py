# ✅ Q11
products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Tablet": 15000,
    "Headphones": 2000,
    "Keyboard": 1000
}

for key in products:
    products[key] = products[key] * 1.10  # Increase by 10%

print("Prices After 10% Increase:", products)


# ✅ Q12
data = {"a": 10, "b": 20, "c": 30}

print("Sum:", sum(data.values()))
print("Maximum:", max(data.values()))
print("Minimum:", min(data.values()))


# ✅ Q13
print("Total Keys:", len(data))


# ✅ Q14
name = input("Enter Name: ")
age = int(input("Enter Age: "))

person = {
    "name": name,
    "age": age
}

person["age"] += 1

print("Updated Dictionary:", person)