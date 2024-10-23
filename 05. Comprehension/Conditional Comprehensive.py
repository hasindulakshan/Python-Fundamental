"""Conditional comprehensions allow to include a condition that filters the elements used in the comprehension."""

# Syntax = [expression for item in iterable if condition]

"""Conditional List Comprehension
"""

# Create a list of squares of even numbers from 0 to 9
evenSquares = [x**2 for x in range(10) if x % 2 == 0]
print(evenSquares)

"""Conditional Set Comprehension
"""

# Create a set of squares of even numbers from 0 to 9
evenSquaresSet = {x**2 for x in range(10) if x % 2 == 0}
print(evenSquaresSet)


"""Conditional Dictionary Comprehension
"""

# Create a dictionary with only even numbers as keys and their squares as values
evenSquareDict = {x: x**2 for x in range(10) if x % 2 == 0}
print(evenSquareDict)
