## OOP is a programming paradigm that uses "objects" and "classes". It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes), which are used to create individual instances of objects.

# Define a class

class Me(): # should be capitalized.
    pass # pass is a keyword that does nothing. It is used when a statement is required syntactically but you do not want any command or code to execute.

# Create an object of the class

me1 = Me() # me is an object of the class Me

me1.name = "Hasindu"
me1.age = 25

print(me1.name, me1.age) 


# Define a class with a attribute

class Me():
    
    def __init__(self): # __init__ is a constructor. It is automatically called always when an object is created.
        print("I am a constructor")
        
    name = "Hasindu"
    age = 25
    
    def set_name(self, name):
        self.name = name
    
    def Run(self):
        print("I am running")
        
    def Walk(self):
        print("I am walking")

  
Me1 = Me()
Me1.set_name("Lakshan")
print(Me1.name)

