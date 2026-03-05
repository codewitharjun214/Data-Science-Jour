import re

print("🟢 PART 1: Basic Pattern Matching")

# 1️⃣ Extract the word "cat"
text = "The cat is sleeping. The dog is barking."
result = re.search(r"\bcat\b", text)
print("1️⃣ Word 'cat':", result.group())

# 2️⃣ Extract all numbers
text = "My marks are 85, 90 and 78."
numbers = re.findall(r"\d+", text)
print("2️⃣ All Numbers:", numbers)

# 3️⃣ Words starting with 'c'
text = "cat car dog cow cup bat"
words = re.findall(r"\bc\w*", text)
print("3️⃣ Words starting with c:", words)

# 4️⃣ All 4-letter words
text = "This book is very good and easy"
words = re.findall(r"\b\w{4}\b", text)
print("4️⃣ 4-letter words:", words)


print("\n🟢 PART 2: search() and match()")

# 5️⃣ Check if string starts with 10 digits
text = "9876543210 is my number"
result = re.match(r"\d{10}", text)
if result:
    print("5️⃣ Starts with 10 digits: Yes")
else:
    print("5️⃣ Starts with 10 digits: No")

# 6️⃣ Extract first email
text = "Contact at help@gmail.com or info@yahoo.com"
result = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
print("6️⃣ First Email:", result.group())


print("\n🟢 PART 3: Using findall()")

# 7️⃣ Extract all phone numbers
text = "Call me at 9876543210 or 9123456789"
numbers = re.findall(r"\b\d{10}\b", text)
print("7️⃣ Phone Numbers:", numbers)

# 8️⃣ Extract all dates
text = "Meeting on 12-03-2026 and 15-04-2026"
dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)
print("8️⃣ Dates:", dates)


print("\n🟢 PART 4: Using sub()")

# 9️⃣ Replace cat with dog
text = "The cat is here."
new_text = re.sub(r"\bcat\b", "dog", text)
print("9️⃣ Replace cat:", new_text)

# 🔟 Hide phone number
text = "My number is 9876543210"
hidden = re.sub(r"\d", "*", text)
print("🔟 Hide Number:", hidden)


print("\n🟢 PART 5: Using split()")

# 1️⃣1️⃣ Split by comma
text = "apple,banana,mango,grapes"
result = re.split(r",", text)
print("1️⃣1️⃣ Split by comma:", result)

# 1️⃣2️⃣ Split by space or comma
text = "apple, banana mango"
result = re.split(r"[,\s]+", text)
print("1️⃣2️⃣ Split by comma or space:", result)


print("\n🟢 PART 6: Practical Questions")

# 1️⃣3️⃣ Extract email from resume
text = "Name: Rahul\nEmail: rahul123@gmail.com\nPhone: 9876543210"
email = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
print("1️⃣3️⃣ Resume Email:", email.group())

# 1️⃣4️⃣ Extract Indian mobile number
text = "Contact: +919876543210"
number = re.search(r"(\+91)?[6-9]\d{9}", text)
print("1️⃣4️⃣ Indian Mobile:", number.group())

print("\n✅ All Regex Tasks Completed Successfully!")

#practice

ad = "arjun is my name 22 is my age"
numbers = re.findall(r"\b\d+\b", ad)
print("this is my age", numbers)