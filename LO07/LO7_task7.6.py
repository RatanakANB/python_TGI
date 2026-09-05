# Task Sheet No. 7.6: Create and Access Nested Tuples
# Description: Create a nested tuple to store fixed student information and retrieve elements.

students = (
    ("Dara", 85),
    ("Sokha", 90),
    ("Vanna", 75)
)

print("Nested student tuple:", students)

# Access individual elements
print("Dara's name         :", students[0][0])
print("Sokha's score       :", students[1][1])
print("Last student's name :", students[-1][0])
print("Number of records   :", len(students))

'''
Sample Output:
Nested student tuple: (('Dara', 85), ('Sokha', 90), ('Vanna', 75))
Dara's name         : Dara
Sokha's score       : 90
Last student's name : Vanna
Number of records   : 3
'''
