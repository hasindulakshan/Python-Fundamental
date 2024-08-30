# Set is a collection of unordered elements. It is mutable and has no duplicate elements.

# Create a set. numbers = {1, 2, 3, 4, 5}

# same to the dictionary, but don't have key-value pairs.
mySet = {"Hello", "World", "Hello"}

# see it will not have duplicate elements. The above set has two "Hello" elements, but it will only have one.
print(mySet)

mySet.add("Python")  # Add a new element to the set.
print(mySet)
mySet.remove("Hello")  # Remove an element from the set.
print(mySet)

# ===============================================================================================

# add two sets together.

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

# Add two sets together. union() method will return a new set with all the elements of both sets.
addedSet = set1.union(set2)
print(addedSet)

# also we can use | (pipe) operator to add two sets together.
addedSet1 = set1 | set2
print(addedSet1)

# ===============================================================================================

# Subtract two sets.

set5 = {1, 2, 3, 4, 5}
set6 = {4, 5, 6, 7, 8}

# Subtract set6 from set5. it will return a new set with the elements that are in set5 but not in set6.
SubtractedSet = set5 - set6
print(SubtractedSet)
