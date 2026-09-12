# Task Sheet No. 9.2: Apply Dictionary Keys, Values, and Items
# Description: Retrieve dictionary keys, values, and key-value pairs using built-in methods.

student = {
    "id": "ST001",
    "name": "Dara",
    "score": 85,
    "course": "Python"
}

print("Total items (len) :", len(student))
print("Keys              :", list(student.keys()))
print("Values            :", list(student.values()))
print("Items (Pairs)     :", list(student.items()))

print()
print("Iterating through items:")
for key, value in student.items():
    print(f"- {key}: {value}")

'''
Sample Output:
Total items (len) : 4
Keys              : ['id', 'name', 'score', 'course']
Values            : ['ST001', 'Dara', 85, 'Python']
Items (Pairs)     : [('id', 'ST001'), ('name', 'Dara'), ('score', 85), ('course', 'Python')]

Iterating through items:
- id: ST001
- name: Dara
- score: 85
- course: Python
'''
