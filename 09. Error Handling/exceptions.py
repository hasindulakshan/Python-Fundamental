from os import path # Import the path module from os module. This module provides a way to work with file paths.


# Positive case

fileName = './Error Handling/Python Error Handling Guide.txt'
if path.exists(fileName):

    with open(fileName) as file:
        print(file.readline())
else:
    print("File not found")


# Negative case

fileName2 = './Error Handling/Python Error Handling Guide2.txt'
if path.exists(fileName2):
    with open(fileName2) as file:
        print(file.readline())
else:
    print("File not found")


