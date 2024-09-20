class Animal:
    def __init__(self, breed):
        print("Animal Constructor: ")
        self.breed = breed

    def talk(self):
        print("Animal Talking")

    def move(self):
        print("Animal Moving")
        
        

class Mamel:
    def __init__(self):
        print("Mamal Constructor: ")
        
    def feed(self):
        print("Feeding Milk")


class Dog(Animal, Mamel):  

    def __init__(self, name="Unknown"):
        super(Dog, self).__init__("Dog")
        self.name = name

    def set_name(self, name):
        self.name = name

    def talk(self):
        super(Dog, self).talk()
        print("Dog is Barking")

    def bark(self, message):
        msg = f"Woof Woof, My name is {self.name}, {message}"
        print(msg)
        
    # we also can override feed method in here


dog1 = Dog("Scooby")
dog1.feed()

