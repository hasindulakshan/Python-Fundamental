# Lists are used to store multiple items in a single variable.

my_list = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]
print(my_list)

# Output 1st element of the list, we can access elements of the list using index of the element.
print(my_list[0])

my_list[0] = 0     # Update the 1st element of the list.
my_list.append(6)  # Add 7 at the end of the list.
print(my_list)

# Add -1 at the index 0 of the list. we can add anywhere in the list using index.
my_list.insert(0, -1)
print(my_list)

# Remove the 5 from the list. Do not use an index, use the value to remove.
my_list.remove(5)
print(my_list)

my_list.pop()    # Remove the last element of the list.
print(my_list)

# We can concatenate two lists. but we can not - or * two lists.
z = my_list + my_list2
print(z)

is_10_in_my_list = 10 in my_list  # Check if 10 is in the list.
print(is_10_in_my_list)

# ===============================================================================================

# Create a new list.

list = [1, 2, 3, 4, 9, 6, 7, 8, 5, 10]

print(len(list))  # Get the length of the list.
# Other methods related to the list are the same as the dictionary. like clear(), copy(), count(), index(), reverse(), sort() etc.

# Count the number of times the value 1 appears in the list.
print(list.count(1))
list.reverse()  # Reverse the list.
print(list)
list.sort()  # Sort the list.
print(list)
