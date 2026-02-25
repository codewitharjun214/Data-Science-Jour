# Practice Questions – Polymorphism
# Basic Level
# Topic - Shape Area Calculator
#  q1

class Shape:
    def area(self):
        print("This is shape area")

class Circle(Shape):
    def area(self):
        print("This is circle area")

class Rectangle(Shape):
    def area(self):
        print("This is rectangle area")

class Triangle(Shape):
    def area(self):
        print("This is triangle area")


# Obj
c = Circle()
r = Rectangle()
t = Triangle()

# Same method name
c.area()
r.area()
t.area()

print("------------------------------------------------")
# q2

class Animal : #main
    def sound(self):
        print(" This is a Animal sound")

class Dog(Animal):
    def sound(self):
        print(" This is a Dog sound")

class Cat(Animal):
    def sound(self):
        print(" This is a Cat sound")

class Cow(Animal):
    def sound(self):
        print(" This is a Cow sound")


#obj

dog = Dog()
cat = Cat()
cow = Cow()

#list
animals = [dog, cat, cow]

#loop
for animal in animals:
    animal.sound()


#Q3
print("--------------------------------------------")

class Payment:
    def pay(self):
        print("This is payment method")

class UPIPayment(Payment):
    def pay(self):
        print("This is UPIPayment method")


class CreditCardPayment(Payment):
    def pay(self):
        print("This is CreditCardPayment method")

class CashPayment(Payment):
    def pay(self):
        print("This is CashPayment method")

# lets create object

upi = UPIPayment()
card = CreditCardPayment()
cash = CashPayment()

# now lets call the methods we created
upi.pay()
card.pay()
cash.pay()


# Intermediate Level
# Q4
print("----------------------------------")

# Base Class
class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        print("Salary calculation method")


# Full Time Employee Class
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full-time employee salary")


# Part Time Employee Class
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Part-time employee salary")


# Creating Objects
emp1 = FullTimeEmployee("Arjun")
emp2 = PartTimeEmployee("Rahul")

emp1.calculate_salary()
emp2.calculate_salary()

# q 5
print("----------------------------")

class Notification:
    def send(self):
        print("Notification method")

class EmailNotification(Notification):
    def send(self):
        print("Email notification method")

class SMSNotification(Notification):
    def send(self):
        print("SMS notification method")

class PushNotification(Notification):
    def send(self):
        print("Push notification method")

# object creation

email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

#method calling

email.send()
sms.send()
push.send()


# question 6
print("--------------------------")
# Parent Class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print("Vehicle is starting...")


# Child Class
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def display_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)
        print("Fuel Type:", self.fuel_type)


# Object Creation
car1 = Car("Honda", 160, "Petrol")

# Method Calling
car1.start()
car1.display_info()

#q7

print("---------------------------")
# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Child Class
class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        # Call Parent Constructor
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


# Object Creation
student1 = Student("Arjun", 21, 101, 85)

# Method Calling
student1.display_details()

#q8
print("---------------------------")

# Parent Class
class Company:
    def company_info(self):
        print("This is ABC Company")


# Child Class (inherits Company)
class Department(Company):
    def department_info(self):
        print("This is IT Department")


# Grandchild Class (inherits Department)
class Employee(Department):
    def employee_info(self):
        print("Employee Name: Arjun")


# Object Creation (Employee class)
emp1 = Employee()

# Accessing All Methods
emp1.company_info()      # From Company
emp1.department_info()   # From Department
emp1.employee_info()     # From Employee

#q9
#example of multilevel inheritance
print("---------------------------")

# Base Class
class School:
    def school_info(self):
        print("This is a School.")


# Child Class
class College(School):
    def college_info(self):
        print("This is a College.")


# Grandchild Class
class University(College):
    def university_info(self):
        print("This is a University.")


# Object Creation
uni = University()

# Accessing All Methods
uni.school_info()      # From School
uni.college_info()     # From College
uni.university_info()  # From University

#q10
# this is example of multiple inheritance
print("--------------------------------------")
class Camera:
    def take_photo(self):
        print("This is a Camera.")

class MusicPlayer:
    def play_music(self):
        print("This is a Music Player.")

class Smartphone(Camera, MusicPlayer):
    def play_music(self):
        print("This is a Smartphone Player.")

#create object
obj = Smartphone()

#call method

obj.take_photo()
obj.play_music()


print("------------------------")
#11
#multiple inheritance

class Designer:
    def designer_info(self):
        print("This is a Designer.")

class Devloper:
    def coding_info(self):
        print("This is a Devloper.")

class Freelancer(Designer, Devloper):
   pass


#lets create obj
free = Freelancer()

#lets call method
free.coding_info()
free.designer_info()

print("---------------------------")

#advance level
#12

# Base Class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        print("Withdrawal method should be overridden.")


# Savings Account
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount >= 1000:   # Minimum balance rule
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Minimum balance of 1000 must be maintained.")
        print("Current Balance:", self.balance)


# Current Account
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount >= -5000:  # Overdraft allowed
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Overdraft limit exceeded.")
        print("Current Balance:", self.balance)


# Testing
s1 = SavingsAccount(101, 5000)
c1 = CurrentAccount(201, 2000)

s1.withdraw(4500)   # Savings rule
c1.withdraw(6000)   # Current rule


#13
# Base Class
print("----------------------------")
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discount(self):
        print("Discount method should be overridden.")


# Electronics Class
class Electronics(Product):
    def get_discount(self):
        discount_price = self.price * 0.90   # 10% discount
        print(f"Electronics Discounted Price: {discount_price}")


# Clothing Class
class Clothing(Product):
    def get_discount(self):
        discount_price = self.price * 0.80   # 20% discount
        print(f"Clothing Discounted Price: {discount_price}")


# Groceries Class
class Groceries(Product):
    def get_discount(self):
        discount_price = self.price * 0.95   # 5% discount
        print(f"Groceries Discounted Price: {discount_price}")


# Testing
p1 = Electronics("Laptop", 50000)
p2 = Clothing("Shirt", 2000)
p3 = Groceries("Rice", 1000)

p1.get_discount()
p2.get_discount()
p3.get_discount()