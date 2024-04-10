# Dictionaries is a collection of key-value pairs.

myDictioanry = {'1000':"Matale", '2000':"Kandy", '3000':"Colombo", '4000':"Galle"} # Create a dictionary.
myDictioanry['1200'] = "Kurunegala"  # Add a new key-value pair to the dictionary.
myDictioanry[10] = "Anuradhapura"  # Add a new key-value pair to the dictionary. we can add any type of key and value. this is integer key.
print(myDictioanry)
 
y = myDictioanry['1000']  # Access the value of the key '1000'. we cannot use index to access the value.
print(y)

print(myDictioanry.keys())  # Get all the keys of the dictionary.
print(myDictioanry.values())  # Get all the values of the dictionary.

# ===============================================================================================

myDictioanry2 = {10 : "Science", 20 : "Maths", 30 : "History", 40 : "English"}
myDictioanry2[50] = ["Biology", "Chemistry"]  # also we can add a list as a value.
print(myDictioanry2)

# ===============================================================================================

myDictioanry3 = {1 : 'A', 2 : 'B'} 

# get() method returns the value of the key. if the key is not in the dictionary, it will return None. but we can set a default value
# to return if the key is not in the dictionary.

getValue = myDictioanry3.get(1)  # Get the value of the key 1.
print(getValue)

getValue2 = myDictioanry3.get(4, 0)  # Get the value of the key 4. if the key is not in the dictionary, return 0.
print(getValue2)

# ===============================================================================================
# Delete a key-value pair from the dictionary.

myDictioanry4 = {1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D'}
print(myDictioanry4)

del myDictioanry4[1]  # Delete the key 1 from the dictionary.
print(myDictioanry4)

myDictioanry4.clear()  # Clear the dictionary.
print(myDictioanry4)

# ===============================================================================================
#  Add complex data types as values to the dictionary.

xDic = {
    "a" : ['Hello', 'Hi', 'Hey'],
    "b" : ('Apple', 'Banana', 'Cherry'),
}

getY = xDic['a']  # Get the value of the key 'a'.
print(getY)

getY.append('Hola')  # Add 'Hola' to the list.
print(getY)

print(xDic)  # see it, you does anything to y, it will affect the dictionary. but it will not affect if "a" is a basic data type. like integer.




