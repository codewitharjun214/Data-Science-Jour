#class is used to define the object
#an object is a real world entity


class Student:

    def __init__(self, name, age, marks, email, roll_no):
        self.name = name
        self.age = age
        self.marks = marks
        self.email = email
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Email:", self.email)
        print("Roll No:", self.roll_no)


# Creating objects
s1 = Student("Rushikesh", 18, 50, "rushikesh@gmail.com", 1)
s2 = Student("Arjun", 21, 50, "arjun@gmail.com", 2)

# Calling method
s1.display()
print("------------")
s2.display()


# Lets make a car object

print("------------")


class Car:
    def __init__(self, make, model, year, price, colour):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour

    def display(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.price)
        print("Colour:", self.colour)


car1 = Car("Ford", "Mustang", 2025, 10000, "Red")
car2 = Car("Toyota", "Fortuner", 2023, 3500000, "Black")

car1.display()
print("------------")
car2.display()


# Third Example

class Trip:
    def __init__(self, whereto, budget , location):
        self.whereto = whereto
        self.budget = budget
        self.location = location


    def display(self):
        print("Whereto:", self.whereto)
        print("Budget:", self.budget)
        print("Location:", self.location)



# Now lets make the object

trip1 = Trip(whereto="Thailand", budget=50000, location= "Pune")
trip2 = Trip(whereto="Austin", budget=10000, location= "Mumbai")
trip1.display()
trip2.display()


