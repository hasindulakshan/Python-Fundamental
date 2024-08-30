
""" Reading a file using the read() method   """

myFile = open("./File input output/dataFile.txt")

print(myFile.read())  # Read the entire file


""" Reading a file using the readline() method   """
print(myFile.readline())  # Read the first line


# using while loop to read the file line by line

while True:
    contents = myFile.readline()
    if not contents:
        break
    print(contents, end="")


# using for loop to read the file line by line

for line in myFile:
    print("Line --> ", line)

myFile.close()
