# Operation Sheet No. 4.1: Create, Access and Manipulate Python Strings
# Program: string_handling.py
# Description: Demonstrates basic procedures to create and manipulate Python string data

# Step 1 & 2 — Create and Display String
course = "Python Programming"
print(course)

# Step 3 — Create a Multiline String
description = """Python is a programming language.
It is easy to learn.
It is widely used."""
print(description)

# Step 4 — Access Characters
print(course[0])
print(course[1])
print(course[-1])

# Step 5 — Slice the String
print(course[0:6])
print(course[:6])
print(course[7:])

# Step 6 — Determine Length
print(len(course))

# Step 7 — Apply Methods
print(course.upper())
print(course.lower())
print(course.replace("Python", "AI"))

# Step 8 — Search
print("Python" in course)
print("Java" not in course)

# Step 9 — Concatenate
s = "favo"
t = "rite"
print(s + t)

# Step 10 — Format String
name = "Dara"
age = 20
print("My name is {} and I am {} years old.".format(name, age))

# Step 11 — Apply Escape Characters
print("Name\tAge\tCourse")
print("Dara\t20\tPython")
print("Python\nProgramming")

'''
Sample Output:
Python Programming
Python is a programming language.
It is easy to learn.
It is widely used.
P
y
g
Python
Python
Programming
18
PYTHON PROGRAMMING
python programming
AI Programming
True
True
favorite
My name is Dara and I am 20 years old.
Name	Age	Course
Dara	20	Python
Python
Programming
'''
