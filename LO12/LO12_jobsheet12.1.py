# Job Sheet No. 12.1: Develop a Modular Student Management Application
# Program: student_management_app.py
# Description: Comprehensive Object-Oriented modular student management project integrating classes, packages, and utilities.

from school.student import Student
from school.utilities import display_header, calculate_total, calculate_average

display_header()

# Create student records
students = [
    Student("ST001", "Dara Sok", "Python Programming", [80, 85, 90]),
    Student("ST002", "Sokha Chea", "Python Programming", [70, 65, 75]),
    Student("ST003", "Vanna Chan", "AI Fundamentals", [45, 50, 48])
]

print("ENROLLED STUDENTS")
for student in students:
    print("-" * 35)
    student.display_info()
    total = calculate_total(student.scores)
    avg = calculate_average(student.scores)
    print("Total Score :", total)
    print("Average     :", f"{avg:.2f}")
    print("Status      :", student.get_result())

# Update course demonstration
print()
print("COURSE UPDATE DEMONSTRATION")
students[2].update_course("Advanced AI")
print(f"Updated {students[2].name}'s course to: {students[2].course}")

'''
Sample Output:
========================================
      STUDENT MANAGEMENT APPLICATION
========================================
ENROLLED STUDENTS
-----------------------------------
ID     : ST001
Name   : Dara Sok
Course : Python Programming
Scores : [80, 85, 90]
Total Score : 255
Average     : 85.00
Status      : Pass
-----------------------------------
ID     : ST002
Name   : Sokha Chea
Course : Python Programming
Scores : [70, 65, 75]
Total Score : 210
Average     : 70.00
Status      : Pass
-----------------------------------
ID     : ST003
Name   : Vanna Chan
Course : AI Fundamentals
Scores : [45, 50, 48]
Total Score : 143
Average     : 47.67
Status      : Fail

COURSE UPDATE DEMONSTRATION
Updated Vanna Chan's course to: Advanced AI
'''
