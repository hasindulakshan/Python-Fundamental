# Function in Python is a block of code that only runs when it is called.

# Define a function for calculating the grade of a student based on the marks

def myFunction(marks, subject):
    
    print("Subject: ", subject)
    if marks < 0 or marks > 100:
        print("Marks are invalid")
    elif marks < 35:
        print("F")
    elif marks < 50:
        print("S")
    elif marks < 60:
        print("C")
    elif marks < 70:
        print("B")
    else:
        print("A")
    
myFunction(45, "Maths") # Calling the function with subject name.
myFunction(marks= 75, subject= "Science") # Calling the function with subject name and marks. its called named argument. in this method we can pass the value of argument in any order.
# myFunction(marks= 75, "Science") # cannot write positional argument after named argument. all named argument should be written after positional argument.)
