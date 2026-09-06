# Job Sheet No. 8.1: Develop a Student Course Set Management Program
# Program: student_course_sets.py
# Description: Comprehensive Python program using sets to process unique student course registration data.

python_students = {"Dara", "Sok", "Rina", "Vanna"}
database_students = {"Sok", "Rina", "Malis"}

print("Python Students:")
for student in sorted(python_students):
    print(student)

# Modify sets
python_students.add("Sophy")
python_students.discard("Vanna")

print()
print("Count:", len(python_students))
print("Is Dara enrolled?", "Dara" in python_students)
print("All Students:", sorted(python_students.union(database_students)))
print("Students in Both:", sorted(python_students.intersection(database_students)))
print("Python Only:", sorted(python_students.difference(database_students)))
print("Only One Course:", sorted(python_students.symmetric_difference(database_students)))

'''
Sample Output:
Python Students:
Dara
Rina
Sok
Vanna

Count: 4
Is Dara enrolled? True
All Students: ['Dara', 'Malis', 'Rina', 'Sok', 'Sophy']
Students in Both: ['Rina', 'Sok']
Python Only: ['Dara', 'Sophy']
Only One Course: ['Dara', 'Malis', 'Sophy']
'''
