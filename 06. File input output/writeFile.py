# In append file, the contents are added to the end of the file.

myFile = open("./File input output/dataFile2.txt",
              "w")  # Open the file in write mode

myFile.write(
    "Opening files: Use open() with the appropriate mode ('r', 'w', 'a', etc.)." + "\n")
myFile.write(
    "Reading files: Use read(), readline(), or readlines() methods." + "\n")
myFile.write(
    "Writing files: Use write() or writelines() methods." + "\n")
myFile.write(
    "Closing files: Always close files after use, preferably with a with statement." + "\n")

myFile.close()  # Close the file
