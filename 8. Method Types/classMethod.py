class Person:
    
    types = ['Person', 'Animal', 'Bird'] # class attribute
    foods = ['Rice', 'Bread', 'Fish'] # class attribute
    
    # Constructor
    def __init__(self, name):
        self.name = name
    
    # instance method    
    def getName(self):
        print(self)
        print("Name: ", self.name)
  
    # class method
    @classmethod
    def getTypes(cls): # cls is a reference to the class itself
        print(cls)
        
    # The first argument to a class method is cls, which refers to the class (Person in this case), not an individual object.


user1 = Person("John")
print(user1.getName) # Prints the method's memory reference, not the result of calling it


print(Person.getTypes)  # Prints the memory reference of the class method
# these types of methods are called class methods.
