class Person:

    def __init___(self, name):
        print("Person class constructor")
        self.name = name

    # instance method
    def print_name(self):
        print("Name: ", self.name)


user = Person("John") # create a instance of the class Person and assign it to the variable user
user.print_name() 

# in instance method, we need to call this method. we need to create object of the class and call the method using the object. calling via instance, because it is a instance method.
