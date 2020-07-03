#OOP
# 4 pillars of OOP
# inheritance
# polymorphism
# encapsulation
# abstraction

class Dog:
    classification = "canine"

    def __init__(self, name, colour): # initialising the class
        self.name = name    # this give the class an attribute
        self.colour = colour

    #method for barking
    def bark(self):
        print(self.name + " said woof woof")

    # method for sleeping
    def sleep(self):
        print(self.name + " said zzzz")

    # method for doing a trick
    def trick(self):
        print(self.name + " did a flip!")

    # method for running
    def run(self):
        print(self.name + " ran away!")

    # method for sitting
    def sit(self):
        print(self.name + " sat down")

    # method for eating
    def eat(self):
        print(self.name + " nom nom nom")



# fido = Dog("douglas", "ginger") #creating an object of our class


# print(fido.colour) # printing an attribute of a class

# create a method inside Dog for sleep, breathe, run, sit
trouble = Dog("trouble", "spotty")

trouble.sleep()
trouble.bark()
trouble.eat()
trouble.trick()

