# Task Sheet No. 12.5: Create and Import a Python Package
# Description: Create structured package directory with __init__.py and import package modules.

from school.student import Student
from school.utilities import calculate_average

scores = [80, 85, 90]
avg = calculate_average(scores)

student = Student("ST001", "Dara", "AI Python", scores)
student.display_info()
print("Calculated Average:", avg)

'''
Sample Output:
ID     : ST001
Name   : Dara
Course : AI Python
Scores : [80, 85, 90]
Calculated Average: 85.0
'''
