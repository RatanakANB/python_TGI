# Job Sheet 2.1: Develop, Test and Debug a Simple Student Grade Program
# Description: Calculate student's total marks and average mark

# Variables
student_name = "Dara"
python_score = 80
database_score = 75
programming_score = 85

# Calculations
total = python_score + database_score + programming_score
average = total / 3

# Expected Output display
print("Student Grade Report")
print("--------------------")
print("Student Name:", student_name)
print("Python:", python_score)
print("Database:", database_score)
print("Programming:", programming_score)
print("Total:", total)
print("Average:", round(average, 1))

'''
Sample Output:
Student Grade Report
--------------------
Student Name: Dara
Python: 80
Database: 75
Programming: 85
Total: 240
Average: 80.0
'''
