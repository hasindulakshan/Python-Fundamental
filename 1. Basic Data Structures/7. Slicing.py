# Slicing in Python list is a way to get a subset of elements from a list. it denote by [start:end]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get the elements from index 2 to 4. This is called slicing.
list2 = list1[2:5]
print(list2)  # Output: [3, 4, 5]

# We can use [:-1] to get all elements without the last element. [-1] to get the last element.

# We can always slice strings, tuples, and sets in the same way as lists. but we cannot slice dictionaries. because dictionaries are unordered.
