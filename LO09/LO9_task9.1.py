# Task Sheet No. 9.1: Create, Print, and Access Python Dictionaries
# Description: Practice dictionary declaration, printing, and key-based access.

student = {
    "id": "ST001",
    "name": "Dara",
    "age": 20,
    "course": "Python"
}

print("Student dictionary:")
print(student)

print()
print("Student Name (bracket notation) :", student["name"])
print("Student Age (bracket notation)  :", student["age"])
print("Course (using get())            :", student.get("course"))
print("Grade (get() with default)      :", student.get("grade", "Not Assigned"))

'''
Sample Output:
Student dictionary:
{'id': 'ST001', 'name': 'Dara', 'age': 20, 'course': 'Python'}

Student Name (bracket notation) : Dara
Student Age (bracket notation)  : 20
Course (using get())            : Python
Grade (get() with default)      : Not Assigned
'''
