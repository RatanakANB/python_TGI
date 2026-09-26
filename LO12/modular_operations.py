# Operation Sheet No. 12.1: Create and Integrate Python Classes, Modules, and Packages
# Program: modular_operations.py
# Description: Complete demonstration of classes, objects, custom modules, packages, and built-in modules.

import math
from school.student import Student
from school.utilities import display_header, calculate_average

display_header()

# Create student object using package class
student = Student("ST001", "Dara", "Python Programming", [80, 85, 90])
student.display_info()
print("Average:", student.get_average())
print("Result :", student.get_result())

# Math built-in demonstration
print()
print("Built-in math sqrt(100):", math.sqrt(100))

'''
Sample Output:
========================================
      STUDENT MANAGEMENT APPLICATION
========================================
ID     : ST001
Name   : Dara
Course : Python Programming
Scores : [80, 85, 90]
Average: 85.0
Result : Pass

Built-in math sqrt(100): 10.0
'''
