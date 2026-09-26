# Worksheet No. 12.1: Python Class, Module, and Package Practice Worksheet
# Description: Practice worksheet evaluating Python OOP concepts, modules, package structures, and built-ins.

# Part A — Class and Object
class Course:
    def __init__(self, title, code):
        self.title = title
        self.code = code

c = Course("Python Development", "PY101")
print("--- Part A: Class and Object ---")
print("Course Title:", c.title)
print("Course Code :", c.code)

# Part B — Built-in Modules
import math
print()
print("--- Part B: Built-in Modules ---")
print("math.factorial(5) =", math.factorial(5))
print("math.ceil(4.2)    =", math.ceil(4.2))

# Part C — Package Structure Concept
print()
print("--- Part C: Package Structure Concept ---")
print("A directory containing __init__.py is recognized as a Python Package.")
print("Modules within the package can be imported using dot notation (e.g., from package.module import Class).")

'''
Sample Output:
--- Part A: Class and Object ---
Course Title: Python Development
Course Code : PY101

--- Part B: Built-in Modules ---
math.factorial(5) = 120
math.ceil(4.2)    = 5

--- Part C: Package Structure Concept ---
A directory containing __init__.py is recognized as a Python Package.
Modules within the package can be imported using dot notation (e.g., from package.module import Class).
'''
