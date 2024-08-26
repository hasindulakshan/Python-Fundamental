# Docstrings provide an explanation of what the function or class does

## Example for Functions

def addNumbers(x, y):
    """
    Add two numbers and return the result.

    Parameters:
    x (int, float): The first number.
    y (int, float): The second number.

    Returns:
    int, float: The sum of the two numbers.
    """
    return x + y

## Example for Classes

class Calculator:
    """
    A class to perform basic arithmetic operations.

    Methods:
    add(a, b): Returns the sum of a and b.
    subtract(a, b): Returns the difference of a and b.
    multiply(a, b): Returns the product of a and b.
    divide(a, b): Returns the quotient of a and b.
    """
    
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a and b. Raises ValueError on division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
