# For Loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. or else we can call foreach loop.

x = [1, 2, 3, 4, 5]  # List

# We use the index to get the value of the list and print the value through an index of the list.
index = 0
for item in x:
    y = x[index]
    print(y)
    index += 1

# We can also use this method to get the value of the list.

# enumerate() function is used to get the index and value of the list.
for index, item in enumerate(x):
    print(index, item)

# if we need to run a loop for a specific number of times then we can use the range() function.

for item in range(0, 10):
    print(type)


# We also can iterate the dictionary using a for loop.

myDictionary = {
    "Age": 25,
    "Name": "Hasindu",
    "Country": "Sri Lanka",
    "City": "Colombo"
}

for key, value in myDictionary.items():
    # items() function is used to get the key and value of the dictionary.
    print(key, value)


# iterate set using for loop

mySet = {
    1,
    "Hasindu",
    3,
    "Lakshan",
    5
}

for item in mySet:
    # set is an unordered collection of items, so the output may not be in the order of the input.
    print(item)


# iterate tuple using for loop

myTuple = ("Hasindu", 2, 3, "BSE", 5)

for item in myTuple:
    # tuple is an ordered collection of items, so the output will be in the order of the input.
    print(item)
