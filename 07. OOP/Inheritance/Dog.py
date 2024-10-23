class Animal:
    def __init__(self, breed):
        print("Animal Constructor: ")
        self.breed = breed

    def talk(self):
        print("Animal Talking")

    def move(self):
        print("Animal Moving")


class Dog(Animal):  # Inheriting from Animal class

    # when calling the constructor of the child class, stop the execution of the parent class constructor
    def __init__(self, name="Unknown"):
        super(Dog, self).__init__("Dog")
        self.name = name

    def set_name(self, name):
        self.name = name

    # Method Overriding - redefine the method of parent class in child class
    def talk(self):
        # we can explicitly call the parent class method. it is not called by default
        super(Dog, self).talk()
        print("Dog is Barking")

    def bark(self, message):
        msg = f"Woof Woof, My name is {self.name}, {message}"
        print(msg)


dog1 = Dog("Scooby")
dog1.talk()
print(dog1.breed)


# Overriding - is a feature to redefine methods of parent class in child classes. 
