# Task Sheet No. 9.3: Change and Add Dictionary Items
# Description: Modify existing dictionary values and add new key-value pairs using direct assignment and update().

student = {
    "name": "Dara",
    "age": 20,
    "course": "Python"
}
print("Original student:", student)

# Change existing value
student["age"] = 21

# Add new key-value pair
student["level"] = "II"

# Update multiple items using update()
student.update({
    "course": "AI Python Developer",
    "score": 90
})

print()
print("Updated student:", student)

'''
Sample Output:
Original student: {'name': 'Dara', 'age': 20, 'course': 'Python'}

Updated student: {'name': 'Dara', 'age': 21, 'course': 'AI Python Developer', 'level': 'II', 'score': 90}
'''
