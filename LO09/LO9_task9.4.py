# Task Sheet No. 9.4: Remove Dictionary Items
# Description: Remove dictionary items using pop, popitem, del, and clear.

student = {
    "id": "ST001",
    "name": "Dara",
    "age": 20,
    "course": "Python",
    "level": "II"
}
print("Initial dictionary:", student)

# pop()
removed_age = student.pop("age")
print()
print("Removed age with pop():", removed_age)
print("After pop('age'):", student)

# popitem() - removes last inserted item
removed_item = student.popitem()
print()
print("Removed item with popitem():", removed_item)
print("After popitem():", student)

# del
del student["course"]
print()
print("After del student['course']:", student)

# clear()
student.clear()
print()
print("After clear():", student)

'''
Sample Output:
Initial dictionary: {'id': 'ST001', 'name': 'Dara', 'age': 20, 'course': 'Python', 'level': 'II'}

Removed age with pop(): 20
After pop('age'): {'id': 'ST001', 'name': 'Dara', 'course': 'Python', 'level': 'II'}

Removed item with popitem(): ('level', 'II')
After popitem(): {'id': 'ST001', 'name': 'Dara', 'course': 'Python'}

After del student['course']: {'id': 'ST001', 'name': 'Dara'}

After clear(): {}
'''
