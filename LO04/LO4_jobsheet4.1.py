# Job Sheet No. 4.1: Develop a Student String Information Processing Program
# Program: student_string_profile.py
# Description: Comprehensive demonstration of Python string creation, indexing, slicing, methods, search, concatenation, formatting, and escape characters.

# Part 1 — Create String Variables
student_name = "Dara Sok"
course = "Python Programming"
institution = "Technical Training Center"

# Part 2 — Create a Multiline String
description = """Python Programming Course
Learning Outcome: String Handling
Level: II"""

# Part 3 — Display Information
print("STUDENT INFORMATION")
print("Name:", student_name)
print("Course:", course)
print("Institution:", institution)

print("\nCOURSE DESCRIPTION")
print(description)

# Part 4 — Access Characters
print("\nSTRING INDEXING")
print("First character:", student_name[0])
print("Second character:", student_name[1])
print("Last character:", student_name[-1])

# Part 5 — Slice Strings
print("\nSTRING SLICING")
print(course[0:6])
print(course[7:])

# Part 6 — Determine Length
print("\nSTRING LENGTH")
print("Student name length:", len(student_name))
print("Course length:", len(course))

# Part 7 — Apply String Methods
print("\nSTRING METHODS")
print("Upper:", course.upper())
print("Lower:", course.lower())
print("Title:", course.title())
print("Replace:", course.replace("Python", "AI Python"))

# Part 8 — Search String
print("\nSTRING SEARCH")
print("Python" in course)
print("Java" in course)

# Part 9 — Required Concatenation
print("\nSTRING CONCATENATION")
s = "favo"
t = "rite"
print(s + t)

# Part 10 — Format Information
print("\nSTRING FORMAT")
print("Student {} is studying {}.".format(student_name, course))

# Part 11 — Escape Characters
print("\nESCAPE CHARACTERS")
print("Name\tCourse")
print("{}\t{}".format(student_name, course))
print("Python\nProgramming")

'''
Sample Output:
STUDENT INFORMATION
Name: Dara Sok
Course: Python Programming
Institution: Technical Training Center

COURSE DESCRIPTION
Python Programming Course
Learning Outcome: String Handling
Level: II

STRING INDEXING
First character: D
Second character: a
Last character: k

STRING SLICING
Python
Programming

STRING LENGTH
Student name length: 8
Course length: 18

STRING METHODS
Upper: PYTHON PROGRAMMING
Lower: python programming
Title: Python Programming
Replace: AI Python Programming

STRING SEARCH
True
False

STRING CONCATENATION
favorite

STRING FORMAT
Student Dara Sok is studying Python Programming.

ESCAPE CHARACTERS
Name	Course
Dara Sok	Python Programming
Python
Programming
'''
