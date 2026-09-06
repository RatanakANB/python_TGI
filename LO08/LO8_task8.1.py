# Task Sheet No. 8.1: Declare, Access and Iterate Python Sets
# Description: Create a Python set containing skills, iterate elements, and check membership.

# Activity 1: Create and display a set with a duplicate value
skills = {"Python", "Database", "Networking", "Python"}
print("Skills set:", skills)

# Activity 2: Iterate through the set
print()
print("Skills list:")
for skill in sorted(skills):
    print(skill)

# Activity 3: Check membership and length
print()
print("'Python' in skills :", "Python" in skills)
print("'AI' in skills     :", "AI" in skills)
print("Number of skills   :", len(skills))

'''
Sample Output:
Skills set: {'Python', 'Database', 'Networking'}

Skills list:
Database
Networking
Python

'Python' in skills : True
'AI' in skills     : False
Number of skills   : 3
'''
