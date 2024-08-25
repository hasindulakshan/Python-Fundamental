# Lists are used to store multiple items in a single variable.

my_list = [1, 2, 3, 4, 5]
my_list2 = [6, 7, 8, 9, 10]
print(my_list)

print(my_list[0])  # Output 1st element of the list, we can access elements of the list using index of the element.

my_list[0] = 0     # Update the 1st element of the list.
my_list.append(6)  # Add 7 at the end of the list.
print(my_list)

my_list.insert(0, -1)  # Add -1 at the index 0 of the list. we can add anywhere in the list using index.
print(my_list)

my_list.remove(5)   # Remove the 5 from the list. not use index, use the value to remove.
print(my_list)

my_list.pop()    # Remove the last element of the list.
print(my_list)

z = my_list + my_list2  # We can concatenate two lists. but we can not - or * two lists.
print(z)

is_10_in_my_list = 10 in my_list  # Check if 10 is in the list.
print(is_10_in_my_list)

# ===============================================================================================


# Create a new list.

list = [1, 2, 3, 4, 9, 6, 7, 8, 5, 10]

print(len(list))  # Get the length of the list.
# other method related to list are same as the dictionary. like clear(), copy(), count(), index(), reverse(), sort() etc.

print(list.count(1))  # Count the number of times the value 1 appears in the list.
list.reverse() # Reverse the list.
print(list)
list.sort()# Sort the list.
print(list)