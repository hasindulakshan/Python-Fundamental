# Exercises

# Implement using for loop

# find the total and average of numbers in a list

list = [-1, -12, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0

for i in list:
    total += i

print("Total is: ", total)

avarage = total / len(list)
print("Avarage is: ", avarage)

# Find the max value in a list

# we can use max = 0, because if all values are negative, it will not work
max = list[0]
for i in list:
    if i > max:
        max = i

print("Max is: ", max)

# Find the min value in a list

min = list[0]

for i in list:
    if min > i:
        min = i

print("Min is: ", min)

# Implement using a while loop

# find the total and average of numbers in a list

list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

count = 0
total2 = 0

while count < len(list2):
    item = list2[count]
    total2 += item

print("Total is: ", total2)
