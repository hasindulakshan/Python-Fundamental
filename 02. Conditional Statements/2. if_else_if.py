# Conditional Statement

# 0 - 30 = Fail
# 30 - 50 = S
# 50 - 60 = C
# 60 - 75 = B
# 75 - 100 = A

marks = 82

if marks >= 0 and marks < 30:
    print("Fail")
elif marks >= 30 and marks < 50:
    print("S")
elif marks >= 50 and marks < 60:
    print("C")
elif marks >= 60 and marks < 75:
    print("B")
elif marks >= 75 and marks <= 100:
    print("A")
else:
    print("Invalid Marks")

# We can also write the above code like this,

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 0 and marks < 30:
    print("Fail")
elif marks < 50:
    print("S")
elif marks < 60:
    print("C")
elif marks < 75:
    print("B")
else:
    print("A")
