# polymorphism
# function same but behaviour different is known as poymorphism


class Animal :
    def speaks(self):
        print("I'm an animal")

class Dog :
    def speaks(self):
        print("I'm a dog")

class Cat :
    def speaks(self):
        print("I'm a cat")

class Person :
    def speaks(self):
        print("I'm a person")

a = Animal()
b = Dog()
c = Cat()
d = Person()

a.speaks()
b.speaks()
c.speaks()
d.speaks()

print("--------------------------------------------------------------------------")
# Example 2

class Payment :
    def pay(self):
        print("I pay a payment")

class Card(Payment):
    def pay(self):
        print("I pay a card")

class UPI(Payment):
    def pay(self):
        print("I pay a UPI")


p = Payment()
u = UPI()
c = Card()

p.pay()
u.pay()
c.pay()



