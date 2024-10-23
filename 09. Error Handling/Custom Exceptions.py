class InvalidAgeError(Exception):
    def __init__(self, error):
        super(InvalidAgeError, self).__init__(error)

class InvalidNameError(Exception):
    def __init__(self, error):
        super(InvalidNameError, self).__init__(error)

class Person:
    def __init__(self, name, age):
        super().__init__()
        
        self.name = name
        self.age = age
        
    
    @staticmethod
    def get_person(name, age):
        if not name:
            # we can raise InvalidNameError instead of Exception, after defining class InvalidNameError
            # raise Exception("Name is required")
            raise InvalidNameError("Name is required")
            print("Error")
        if age < 0 or age > 120:
            # also can use for age: raise InvalidAgeError("Age is invalid") after defining class InvalidAgeError
            raise InvalidAgeError("Age is invalid")
            return
        
        return Person(name, age)
    
try:
    person = Person.get_person("", -31)
    print(person)
except Exception as e:
    print("Error: ", e)