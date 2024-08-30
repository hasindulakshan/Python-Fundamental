# If-Else Statement - used to execute a block of code if a condition is true and another block of code if it is false.

# Indentation - is a space at the beginning of a code line. It is used to define a block of code.

x = 10
y = 20

if x >= 25:
    print("You Are Selected")
else:
    print("You Are Not Selected")

# Output: You Are Not Selected, it depends on the value of x.

height = 5.7

if height >= 5.5:
    job = "Security"
else:
    job = "Labor"

print(job)

# We can write the above code in one line like this,

# this method is called Ternary Operator
job = "Security" if height >= 5.5 else "Labor"
print(job)
