class InvalidAgeError(Exception):
    def __init__(self, error):
        super(InvalidAgeError, self).__init__(error)

class Person:
    def __init__(self, name, age):
        super().__init__()
        
        self.name = name
        self.age = age
        
    
    @staticmethod
    def get_person(name, age):
        if not name:
            # we can raise InvalidAgeError instead of Exception, after defining class InvalidAgeError
            # raise Exception("Name is required")
            raise InvalidAgeError("Name is required")
            print("Error")
        if age < 0 or age > 120:
            raise InvalidAgeError("Age is invalid")
            return
        
        return Person(name, age)
    
try:
    person = Person.get_person("", -31)
    print(person)
except Exception as e:
    print("Error: ", e)