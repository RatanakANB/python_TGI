# Task Sheet No. 11.3: Apply return, Default Parameters, and Keyword Arguments
# Description: Functions returning results, default fallback parameters, and keyword arguments.

# Practical Exercise A — return
def add(a, b):
    return a + b

result = add(5, 10)
print("Result of add(5, 10):", result)

# Practical Exercise B — Default Parameter
print()
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Dara")

# Practical Exercise C — Keyword Arguments
print()
def student_info(name, age, course):
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)

student_info(course="Python", age=20, name="Dara")

'''
Sample Output:
Result of add(5, 10): 15

Hello Student
Hello Dara

Name   : Dara
Age    : 20
Course : Python
'''
