"""Default values in python function is used to set the default value of the argument.
If the value of the argument is not passed to the function then the default value is used."""

def myFunction(marks, subject="Unknown"): # Default value of subject is "Unknown"
    
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
    


myFunction(45) # Calling the function with subject name. in this method we can pass only one argument. because we have set default value for subject.
myFunction(marks= 75, subject= "Science") # Calling the function with subject name and marks. its called named argument. we can change the default value of subject.


"""we cannot pass the value of subject without passing the value of marks. because we have not set the default value of marks. 
also we cannot create parameter without default value after the parameter with default value."""