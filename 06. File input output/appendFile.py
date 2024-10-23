# In append file, the contents are added to the end of the file.


with open("test.txt", "a") as myFile:
    myFile.write(
        "Opening files: Use open() with the appropriate mode ('r', 'w', 'a', etc.)." + "\n")
    myFile.write(
        "Reading files: Use read(), readline(), or readlines() methods." + "\n")
    myFile.write(
        "Writing files: Use write() or writelines() methods." + "\n")
    myFile.write(
        "Closing files: Always close files after use, preferably with a with statement." + "\n")

# in this method, automatically closes the file after the block of code is executed. we dont need to close the file explicitly. its called context manager.
