# Job Sheet No. 3.5: Develop a Python Syntax Demonstration Program

# Variables
student_name = "Dara"
age = 20
average_score = 85.5
complex_number = 2 + 3j
is_student = True

# Display variable values
print("Student Name:", student_name)
print("Age:", age)
print("Average Score:", average_score)
print("Complex Number:", complex_number)
print("Student Status:", is_student)

# DATA TYPES
print("\nDATA TYPES")
print(type(student_name))
print(type(age))
print(type(average_score))
print(type(complex_number))
print(type(is_student))

# ARITHMETIC OPERATORS
a = 5
b = 10
print("\nARITHMETIC OPERATORS")
print("A + B =", a + b)
print("B - A =", b - a)
print("A * B =", a * b)
print("B / A =", b / a)

# COMPARISON OPERATORS
print("\nCOMPARISON OPERATORS")
print("A < B:", a < b)
print("A > B:", a > b)
print("A == B:", a == b)
print("A != B:", a != b)

# LOGICAL OPERATORS
print("\nLOGICAL OPERATORS")
print(a < b and b == 10)
print(a > b or b == 10)
print(not a > b)

# INDENTATION
print("\nINDENTATION")
if a < b:
    print("A is less than B")

'''
Sample Output:
Student Name: Dara
Age: 20
Average Score: 85.5
Complex Number: (2+3j)
Student Status: True

DATA TYPES
<class 'str'>
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'bool'>

ARITHMETIC OPERATORS
A + B = 15
B - A = 5
A * B = 50
B / A = 2.0

COMPARISON OPERATORS
A < B: True
A > B: False
A == B: False
A != B: True

LOGICAL OPERATORS
True
True
True

INDENTATION
A is less than B
'''
