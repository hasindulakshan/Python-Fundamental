# static methods in Python are similar to class methods, but they don't receive any additional arguments; they are identical to normal functions that belong to a class.

class Person:
    
    types = ['Person', 'Animal', 'Bird'] 
    foods = ['Rice', 'Bread', 'Fish'] 
    
    # Constructor
    def __init__(self, name):
        self.name = name
    
    # instance method    
    def getName(self):
        print(self)
        print("Name: ", self.name)
  
    # class method
    @classmethod
    def getTypes(cls): 
        print(cls)
    
    @staticmethod
    def getFoods():
        print("Foods: ", Person.foods)
        


user1 = Person("John")
print(user1.getName) 

user1.getFoods()
