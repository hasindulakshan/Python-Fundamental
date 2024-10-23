""" In Python, *args and **kwargs are used to pass a variable number of arguments to a function. """

# *args is used to pass a variable number of non-keyword arguments to a function.It allows you to pass any number of positional arguments


def my_function(*args):
    for arg in args:
        print(arg)


my_function(1, 2, 3, 4, 5)


# **kwargs is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of named arguments, which are then packed into a dictionary.

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


my_function(name="Hasindu", age=22, city="Kandy")

""" Combining *args and **kwargs in a function """


# packed arguments/positional arguments should be written first.
def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


my_function(1, 2, 3, 4, 5, name="Hasindu", age=22)

# You can use both *args and **kwargs in the same function to handle both positional and keyword arguments.

""" Practice - 5 values and pass it to function and print the sum of all values in the list."""

##


def sum(*list):  # *list is used to pass multiple values to the function.
    total = 0
    for i in list:
        total += i
    print(total)  # print the sum of all values in the list.


sum(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
