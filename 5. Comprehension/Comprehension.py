"""Comprehension is a way to create data structure using other data structure
   (comprehensions provide a concise way to create data structures such as lists, sets, and dictionaries from existing data structures.)
"""
# Syntax = [expression for item in iterable]

"""List Comprehension - create lists by iterating over an iterable and specifying the expression to be included in the list
"""

# Create list using values of other list

listA = [1, 2, 3, 4, 5]
listB = [i for i in listA]  # Create listB using listA
print(listA, listB)

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

"""Set Comprehension - Similar to list comprehensions, but it creates a set instead of a list
"""

# Create a set of squares of numbers from 0 to 9
squareSet = {x**2 for x in range(10)}
print(squareSet)

"""Dictionary Comprehension - create dictionaries by iterating over an iterable and specifying key-value pairs
"""

# Syntax = {key_expression: value_expression for item in iterable}

# Create a dictionary with numbers as keys and their squares as values
squareDict = {x: x**2 for x in range(10)}
print(squareDict)
