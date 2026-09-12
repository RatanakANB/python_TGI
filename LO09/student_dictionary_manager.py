# Job Sheet No. 9.1: Develop a Student Record Management Program Using Dictionaries
# Program: student_dictionary_manager.py
# Description: Complete Python program using dictionaries to manage structured student information.

# 1. Create a student dictionary
student = {
    "id": "ST001",
    "name": "Dara",
    "age": 20,
    "course": "Python",
    "score": 85
}

print("STUDENT DICTIONARY")
print(student)

# 2. Access data
print()
print("ACCESS DATA")
print("Name:", student["name"])
print("Course:", student.get("course"))

# 3. Keys, values and items
print()
print("KEYS, VALUES AND ITEMS")
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# 4. Modify data
print()
print("MODIFY DATA")
student["age"] = 21
student["level"] = "II"
student.update({
    "course": "AI Basic Python Developer",
    "score": 88
})
print(student)

# 5. Remove data
print()
print("REMOVE DATA")
removed_age = student.pop("age")
print("Removed age:", removed_age)
print(student)

# 6. Membership
print()
print("MEMBERSHIP")
print("name in student:", "name" in student)
print("email not in student:", "email" not in student)

# 7. Nested dictionary
print()
print("NESTED DICTIONARY")
students = {
    "ST001": {
        "name": "Dara",
        "score": 85,
        "course": "Python"
    },
    "ST002": {
        "name": "Sokha",
        "score": 90,
        "course": "Python"
    },
    "ST003": {
        "name": "Vanna",
        "score": 75,
        "course": "Python"
    }
}
for sid, info in students.items():
    print(f"- {sid}: {info['name']} | Score: {info['score']} | Course: {info['course']}")

'''
Sample Output:
STUDENT DICTIONARY
{'id': 'ST001', 'name': 'Dara', 'age': 20, 'course': 'Python', 'score': 85}

ACCESS DATA
Name: Dara
Course: Python

KEYS, VALUES AND ITEMS
Keys: ['id', 'name', 'age', 'course', 'score']
Values: ['ST001', 'Dara', 20, 'Python', 85]
Items: [('id', 'ST001'), ('name', 'Dara'), ('age', 20), ('course', 'Python'), ('score', 85)]

MODIFY DATA
{'id': 'ST001', 'name': 'Dara', 'age': 21, 'course': 'AI Basic Python Developer', 'score': 88, 'level': 'II'}

REMOVE DATA
Removed age: 21
{'id': 'ST001', 'name': 'Dara', 'course': 'AI Basic Python Developer', 'score': 88, 'level': 'II'}

MEMBERSHIP
name in student: True
email not in student: True

NESTED DICTIONARY
- ST001: Dara | Score: 85 | Course: Python
- ST002: Sokha | Score: 90 | Course: Python
- ST003: Vanna | Score: 75 | Course: Python
'''
