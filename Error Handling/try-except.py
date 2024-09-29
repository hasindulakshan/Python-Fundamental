# try-except block to handle exceptions

x = 10
y = 0

try:
    z = x / y
    print(z)
except:
    print("Error: Division by zero")