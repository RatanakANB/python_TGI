# Worksheet No. 9.1: Python Dictionary Practice and Verification Worksheet
# Description: Practice worksheet evaluating Python dictionary creation, methods, modification, and nested structures.

# Part A — Create a Dictionary
student = {
    "id": "ST001",
    "name": "Dara",
    "age": 20,
    "course": "Python"
}
print("--- Part A: Create a Dictionary ---")
print("student =", student)

# Part B — Access Values
print()
print("--- Part B: Access Values ---")
print("student['name']       =", student["name"])
print("student.get('course') =", student.get("course"))

# Part C — Keys, Values, and Items
print()
print("--- Part C: Keys, Values, and Items ---")
print("Keys   =", list(student.keys()))
print("Values =", list(student.values()))
print("Items  =", list(student.items()))

# Part D — Modify and Add
student["age"] = 21
student["grade"] = "A"
print()
print("--- Part D: Modify and Add ---")
print("Modified student =", student)

# Part E — Remove Items
removed_id = student.pop("id")
print()
print("--- Part E: Remove Items ---")
print("Removed id =", removed_id)
print("After pop  =", student)

# Part F — Membership
print()
print("--- Part F: Membership ---")
print("'name' in student  =", "name" in student)
print("'id' not in student =", "id" not in student)

'''
Sample Output:
--- Part A: Create a Dictionary ---
student = {'id': 'ST001', 'name': 'Dara', 'age': 20, 'course': 'Python'}

--- Part B: Access Values ---
student['name']       = Dara
student.get('course') = Python

--- Part C: Keys, Values, and Items ---
Keys   = ['id', 'name', 'age', 'course']
Values = ['ST001', 'Dara', 20, 'Python']
Items  = [('id', 'ST001'), ('name', 'Dara'), ('age', 20), ('course', 'Python')]

--- Part D: Modify and Add ---
Modified student = {'id': 'ST001', 'name': 'Dara', 'age': 21, 'course': 'Python', 'grade': 'A'}

--- Part E: Remove Items ---
Removed id = ST001
After pop  = {'name': 'Dara', 'age': 21, 'course': 'Python', 'grade': 'A'}

--- Part F: Membership ---
'name' in student  = True
'id' not in student = True
'''
