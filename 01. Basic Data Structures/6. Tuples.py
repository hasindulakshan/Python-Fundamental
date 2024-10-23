# Tuple is a collection of items which is ordered and unchangeable. Allows duplicate members.
# Tuples are used to store multiple items in a single variable.

# Create a tuple.

myTuple = ("Hasindu", 175, "Matale", 22)  # Create a tuple.
print(myTuple)
print(type(myTuple))  # Get the type of the myTuple.

# ===============================================================================================

# Access the elements of the tuple.

name = myTuple[0]  # Access the first element of the tuple.
print("Name: ", name)

print("Height: ", myTuple[1])  # Access the second element of the tuple.
print("City: ", myTuple[2])  # Access the third element of the tuple.
print("Age: ", myTuple[3])  # Access the fourth element of the tuple.

# ===============================================================================================

# Count the number of times the value "Hasindu" appears in the tuple.
print(myTuple.count("Hasindu"))

# Assign values to multiple variables.

hasindu = ("Hasindu", 175, "Matale", 22)
# Assign the values of the tuple to the variables.
name, height, city, age = hasindu
print(name, height, city, age)  # Print the values of the variables.
