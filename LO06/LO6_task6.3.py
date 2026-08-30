# Task Sheet No. 6.3: Determine List Length and Add List Elements
# Description: Determine the number of elements and add new elements using len, append, insert, and extend.

students = ["Dara", "Sokha"]
print("Initial list:", students)

# Determine length
print("Number of students:", len(students))

# append()
students.append("Vanna")
print("After append:", students)

# insert()
students.insert(1, "Malis")
print("After insert at index 1:", students)

# extend()
students.extend(["Bopha", "Chenda"])
print("After extend:", students)

# Updated length
print("Final number of students:", len(students))

'''
Sample Output:
Initial list: ['Dara', 'Sokha']
Number of students: 2
After append: ['Dara', 'Sokha', 'Vanna']
After insert at index 1: ['Dara', 'Malis', 'Sokha', 'Vanna']
After extend: ['Dara', 'Malis', 'Sokha', 'Vanna', 'Bopha', 'Chenda']
Final number of students: 6
'''
