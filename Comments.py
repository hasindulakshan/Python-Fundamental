# ==>   Single line comment using # symbol
# ==>   Multi line comment using ''' or """

"Hello World" # stings are enclosed in double quotes without assigned to a variable, Python interpreter automatically ignore it. so we can use it as a comment.

# Type hinting

def add(a: int, b: int) -> int:  # a and b are integers and the return type is also integer, but this is not enforced by the interpreter. we can use any type of data.
    return a + b

print(add(10, 20)) # 30