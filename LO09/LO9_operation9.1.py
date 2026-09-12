# Operation Sheet No. 9.1: Create, Access, and Manipulate Python Dictionaries
# Program: dictionary_operations.py
# Description: Demonstrates standard procedures for creating and manipulating Python dictionary data.

# Step 1: Create dictionary
student = {
    "id": "ST001",
    "name": "Dara",
    "age": 20,
    "course": "Python"
}
print("Original dictionary:", student)

# Step 2: Access values
print()
print("Name   :", student["name"])
print("Course :", student.get("course"))

# Step 3: Keys, values, and items
print()
print("Keys   :", list(student.keys()))
print("Values :", list(student.values()))
print("Items  :", list(student.items()))

# Step 4: Modify, add and update
student["age"] = 21
student["level"] = "II"
student.update({"course": "AI Basic Python Developer"})
print()
print("After modification:", student)

# Step 5: Remove item
student.pop("age")
print()
print("After pop('age'):", student)

# Step 6: Membership check
print()
print("'name' in student :", "name" in student)

# Step 7: Nested dictionary
students = {
    "student1": {
        "name": "Dara",
        "score": 85
    },
    "student2": {
        "name": "Sokha",
        "score": 90
    }
}
print()
print("Nested student1 name:", students["student1"]["name"])

'''
Sample Output:
Original dictionary: {'id': 'ST001', 'name': 'Dara', 'age': 20, 'course': 'Python'}

Name   : Dara
Course : Python

Keys   : ['id', 'name', 'age', 'course']
Values : ['ST001', 'Dara', 20, 'Python']
Items  : [('id', 'ST001'), ('name', 'Dara'), ('age', 20), ('course', 'Python')]

After modification: {'id': 'ST001', 'name': 'Dara', 'age': 21, 'course': 'AI Basic Python Developer', 'level': 'II'}

After pop('age'): {'id': 'ST001', 'name': 'Dara', 'course': 'AI Basic Python Developer', 'level': 'II'}

'name' in student : True

Nested student1 name: Dara
'''
