# Function in python is a block of code that only runs when it is called.

# Define a function for calculating the grade of a student based on the marks

def myFunction(marks, subject = "unknown"):
    
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
    

myFunction(66) # Calling the function.
myFunction(45, "Maths") # Calling the function with subject name.
myFunction(marks= 75, subject= "Science") # Calling the function with subject name and marks. its called named argument.


## 5 values and pass it to function and print the sum of all values in the list. packed arguments.

def sum(*list): # *list is used to pass multiple values to the function.
    total = 0
    for i in list:
        total += i
    print(total) # print the sum of all values in the list.
    

sum(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)