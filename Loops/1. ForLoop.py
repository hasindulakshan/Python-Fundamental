# For Loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. or else we can call foreach loop.

x = [1, 2, 3, 4, 5] # List

index = 0 # we use index to get the value of the list and print tha value through index of the list.
for item in x:
    y = x[index]
    print(y)
    index += 1
    
# we can also use this method to get the value of the list.

for index, item in enumerate(x): # enumerate() function is used to get the index and value of the list.
    print(index, item)

# if we need to run a loop for a specific number of times then we can use range() function.

for item in range(0, 10):
    print(type)


## we also can iterate dictionary using for loop.

myDictionary = {
    "Age": 25,
    "Name": "Hasindu", 
    "Country": "Sri Lanka",
    "City": "Colombo"
}

for key, value in myDictionary.items(): 
    print(key, value) # items() function is used to get the key and value of the dictionary.


## iterate set using for loop

mySet = {
    1,
    "Hasindu",
    3,
    "Lakshan",
    5
}

for item in mySet:
    print(item) # set is an unordered collection of items, so the output may not be in the order of the input.


## iterate tuple using for loop

myTuple = ("Hasindu", 2, 3, "BSE", 5) 

for item in myTuple:
    print(item) # tuple is an ordered collection of items, so the output will be in the order of the input.