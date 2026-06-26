#error handling (exception handling)

# print("hello")
#
# print((3+2)*7)

try:
   num = int(input("Enter a number: "))
   result = 10/num
   print(result)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Value Error")
finally:
    print("End of the program")

try:
    x = int("ABC")
except Exception as e:
    print("error occoured",e)

age = int(input("Enter a number: "))
if age < 0:
    raise ValueError("Age cannot be negative")
print("age is valid")


