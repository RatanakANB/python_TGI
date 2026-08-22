# Task Sheet No. 3.1: Identify Python Variables, Keywords and Data Types

# Practical Exercise
student_name = "Dara"
age = 20
average = 85.5
complex_number = 2 + 3j
is_student = True

# Display each value and its type
print("Variable Values and Data Types:")
print(f"student_name: {student_name} -> {type(student_name)}")
print(f"age: {age} -> {type(age)}")
print(f"average: {average} -> {type(average)}")
print(f"complex_number: {complex_number} -> {type(complex_number)}")
print(f"is_student: {is_student} -> {type(is_student)}")

# Python Keywords Check
import keyword
print("\nKeywords Check:")
words = ["if", "student", "class", "score", "while", "total"]
for word in words:
    print(f"Is '{word}' a keyword? {keyword.iskeyword(word)}")

'''
Sample Output:
Variable Values and Data Types:
student_name: Dara -> <class 'str'>
age: 20 -> <class 'int'>
average: 85.5 -> <class 'float'>
complex_number: (2+3j) -> <class 'complex'>
is_student: True -> <class 'bool'>

Keywords Check:
Is 'if' a keyword? True
Is 'student' a keyword? False
Is 'class' a keyword? True
Is 'score' a keyword? False
Is 'while' a keyword? True
Is 'total' a keyword? False
'''
