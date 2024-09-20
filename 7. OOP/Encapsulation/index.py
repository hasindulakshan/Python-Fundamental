class Person:
    def __init__(self, name):
        self.name = name # name is public attribute
        # self.age = 22 
        self.__age = 22 # Now, age is private attribute
        self._city = "Kandy" # Now, city is protected attribute
    
    # setter method
    def set_age(self, age):
        self.__age = age
    
    # getter method   
    def get_age(self):
        return self.__age

    def sleep(self):
        print(self.name,"is Sleeping")
        



        
user = Person("John")
user.sleep()

# we also can access the age attribute directly and change it, which is not good. To prevent this, we can use encapsulation (Access Modifiers => Public, Private, Protected)

# print(user.age) 
# user.age = 25
# print(user.age)

# after added get_age method, we can access the age attribute indirectly
print(user.get_age())

# after added set_age method, we can change the age attribute indirectly
user.set_age(25)
print("after set age:", user.get_age())

## This method called Encapsulation or Data Hiding. in this method, we can restrict the access to some components of the class.



class Student(Person):
    def __init__(self, name):
        super(Student, self).__init__(name)
    
    # def print_age(self):
    #     print("Age: ", self.__age)
        
    def print_city(self):
        print("City: ", self._city)
        
user2 = Student("Alice")
           
# user2.print_age() # Also we cant access the private attribute in child class. want we to access the private attribute in child class, we can use protected attribute.

user2.print_city() # Also we can access the protected attribute in child class.



# private = only access within the class
# protected = access within the class and child classes
# public = access within the class, child classes and outside the class