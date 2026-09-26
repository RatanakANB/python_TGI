# Task Sheet No. 12.3: Create a Module Containing a Python Class
# Description: Import class from standalone module student.py and instantiate objects.

from student import Student

student1 = Student("Dara", 85)
student1.display_info()
print("Result:", student1.get_result())

'''
Sample Output:
Name  : Dara
Score : 85
Result: Pass
'''
