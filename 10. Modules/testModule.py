import createModule # Importing the module. module name is file name without .py extension

print(createModule.get_name()) # calling the function through module
print(createModule.get_age())

print(dir(createModule)) # This will print all the functions and variables in the module. it will print as a list