# Task Sheet No. 9.6: Create and Manage Nested Dictionaries
# Description: Create a nested dictionary to store student records and access/modify multi-level values.

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

print("Nested student records:")
print(students)

# Access nested items
print()
print("ST001 name  :", students["ST001"]["name"])
print("ST002 score :", students["ST002"]["score"])

# Modify nested value
students["ST003"]["score"] = 80
print("Updated ST003 score:", students["ST003"]["score"])

# Add new key-value pair in nested dictionary
students["ST001"]["level"] = "II"
print("ST001 after adding level:", students["ST001"])

'''
Sample Output:
Nested student records:
{'ST001': {'name': 'Dara', 'score': 85, 'course': 'Python'}, 'ST002': {'name': 'Sokha', 'score': 90, 'course': 'Python'}, 'ST003': {'name': 'Vanna', 'score': 75, 'course': 'Python'}}

ST001 name  : Dara
ST002 score : 90
Updated ST003 score: 80
ST001 after adding level: {'name': 'Dara', 'score': 85, 'course': 'Python', 'level': 'II'}
'''
