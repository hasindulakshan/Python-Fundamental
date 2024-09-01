# self keyword is a reference to the current instance of the class, and is used to access variables that belong to the class.

# Define a class with an attribute

class Dog():

    # this is a constructor its called automatically when an object is created. it should be define with the __init__ method.
    # default value of name is "Unknown. if you forget to pass a name, it will be set to "Unknown"
    def __init__(self, name="Unknown"):
        self.name = name

    def set_name(self, name):
        self.name = name

    def bark(self, message):
        msg = f"{self.name} says {message}"
        print(msg)

    def walk(self, path):
        msg = f"{self.name} is walking on {path}"
        print(msg)


# Create an object of the class dog1
dog1 = Dog("Tommy")
dog1.bark("I am barking")
dog1.walk("the road")


# Create an object of the class dog2
dog2 = Dog()  # name is automatically set to "Unknown"
dog2.bark("I am barking")
dog2.walk("the road")
