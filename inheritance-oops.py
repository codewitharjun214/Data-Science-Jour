# parent class properties are transfer to the child class is known as inheritance
# there are five types of inheritance
# Single inheritance
# One parent → One child

class Parent :
    def skill(self):
        print("Driving")


class Child(Parent):
    def studies(self):
        print("Studying")

d = Child()

d.skill()
d.studies()


# Example 2
print("--------------------------------------------------------------------------------------")

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):   # Dog inherits Animal
    def bark(self):
        print("Dog is barking")

d = Dog()

d.eat()   # from Animal class
d.bark()  # from Dog class



# multilevel
# Grandparent → Parent → Child
print("---------------------")

class GrandParent :
    def show(self):
        print("GrandParent is show")

class Parent(GrandParent):
    def skiling(self):
        print("Parent is skiling")

class Child(Parent):
    def studies(self):
        print("Child is studying")

c = Child()
p = Parent()

p.skiling()
p.show()

c.show()
c.studies()
c.skiling()


# multiple inheritance
# Child inherits from more than one parent
print("-------------------------------------------------------")

class Mother :
    def eat(self):
        print("Mother is eating")

class Father:
    def drive(self):
        print("Father is eating")

class Child(Mother,Father):
    def learn(self):
        print("Child is eating")

c = Child()

c.learn()
c.drive()
c.eat()


# Hierarchical Inheritance
# One parent → Many children
print("--------------------------------------------------------------------------")

class Parent:
    def property1(self):
        print("Property")

class Child1(Parent):
    def property2(self):
        print("Property2")

class Child2(Parent):
    def property3(self):
        print("Property3")

c = Child1()
c.property1()

c = Child2()
c.property1()


# Hybrid Inheritance
# made by combination
class Grandparent:
    def house(self):
        print("Grandparent's house")

class Parent(Grandparent):
    def car(self):
        print("Parent's car")

class Child1(Parent):
    def bike(self):
        print("Child1's bike")

class Child2(Parent, Child1):   # Hybrid inheritance
    pass

c = Child2()

c.house()
c.car()
c.bike()