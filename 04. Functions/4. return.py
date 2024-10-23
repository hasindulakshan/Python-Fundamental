""" Grade statement in Python used to exit a function and go back to the place from where it was called. """


def get_grade(marks):
    if marks < 0 or marks > 100:
        grade = None
    elif marks >= 90:
        grade = 'A'
    elif marks >= 80:
        grade = 'B'
    elif marks >= 70:
        grade = 'C'
    elif marks >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade


grade = get_grade(85)
print(grade)
