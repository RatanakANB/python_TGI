# Task Sheet No. 6.5: Create and Access Nested Lists
# Description: Create a nested list for storing student names and scores, and retrieve/modify specified info.

students = [
    ["Dara", 85],
    ["Sokha", 90],
    ["Vanna", 75]
]

print("Nested list of students:", students)

# Access individual elements
print("Dara's name   :", students[0][0])
print("Sokha's score :", students[1][1])

# Modify a nested value
students[2][1] = 80
print("After updating Vanna's score to 80:", students)

'''
Sample Output:
Nested list of students: [['Dara', 85], ['Sokha', 90], ['Vanna', 75]]
Dara's name   : Dara
Sokha's score : 90
After updating Vanna's score to 80: [['Dara', 85], ['Sokha', 90], ['Vanna', 80]]
'''
