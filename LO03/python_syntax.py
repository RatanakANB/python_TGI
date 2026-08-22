# Operation Sheet No. 3.1: Create Variables, Identify Data Types and Apply Python Operators

student_name = "Dara"
age = 20
average = 85.5
is_student = True

print(student_name)
print(age)
print(average)
print(is_student)

print(type(student_name))
print(type(age))
print(type(average))
print(type(is_student))

a = 5
b = 10
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(a < b and b == 10)
print(a > b or b == 10)
print(not a > b)

if a < b:
    print("A is less than B")

'''
Sample Output:
Dara
20
85.5
True
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
True
False
False
True
True
True
False
A is less than B
'''
