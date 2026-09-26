# Task Sheet No. 12.1: Create Classes and Objects
# Description: Define class syntax, initialize attributes with __init__, and instantiate multiple objects.

class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score

student1 = Student("ST001", "Dara", 85)
student2 = Student("ST002", "Sokha", 90)

print("Student 1:")
print("ID    :", student1.student_id)
print("Name  :", student1.name)
print("Score :", student1.score)

print()
print("Student 2:")
print("ID    :", student2.student_id)
print("Name  :", student2.name)
print("Score :", student2.score)

'''
Sample Output:
Student 1:
ID    : ST001
Name  : Dara
Score : 85

Student 2:
ID    : ST002
Name  : Sokha
Score : 90
'''
