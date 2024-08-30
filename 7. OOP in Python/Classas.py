"""OOP is a programming paradigm that uses "objects" and "classes".
   It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes), which are used to create individual instances of objects.
"""

# Define a class


class Person():  # should be capitalized.
    pass  # pass is a keyword that does nothing. It is used when a statement is required syntactically but you do not want any command or code to execute.


# Create an object of the class

person1 = Person()  # me is an object of the class Me

person1.name = "Your Name"
person1.age = 22

print(person1.name, person1.age)


# Define a class with an attribute

class Person():

    # __init__ is a constructor. It is automatically called always when an object is created.
    def __init__(self):
        print("I am a constructor")

    name = "Your Name"
    age = 25

    def set_name(self, name):
        self.name = name

    def Run(self):
        print("I am running")

    def Walk(self):
        print("I am walking")


person2 = Person()
person2.set_name("Your First Name")
print(person2.name)
