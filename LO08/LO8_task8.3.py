# Task Sheet No. 8.3: Apply Python Set Operations
# Description: Compare two student course registration sets using union, intersection, difference, and symmetric difference.

python_students = {"Dara", "Sok", "Rina", "Vanna"}
database_students = {"Sok", "Rina", "Malis"}

print("Python students   :", python_students)
print("Database students :", database_students)

# Union: all unique students
print()
print("Union (All students)                :", python_students.union(database_students))

# Intersection: students enrolled in both
print("Intersection (Students in both)     :", python_students.intersection(database_students))

# Difference: students only in Python
print("Difference (Python only)            :", python_students.difference(database_students))

# Symmetric Difference: students in only one course
print("Symmetric Difference (Only one)     :", python_students.symmetric_difference(database_students))

'''
Sample Output:
Python students   : {'Dara', 'Sok', 'Rina', 'Vanna'}
Database students : {'Sok', 'Rina', 'Malis'}

Union (All students)                : {'Dara', 'Sok', 'Rina', 'Vanna', 'Malis'}
Intersection (Students in both)     : {'Sok', 'Rina'}
Difference (Python only)            : {'Dara', 'Vanna'}
Symmetric Difference (Only one)     : {'Dara', 'Vanna', 'Malis'}
'''
