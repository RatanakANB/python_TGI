# Job Sheet No. 7.1: Develop a Fixed Student Record Program Using Tuples
# Program: student_tuple_manager.py
# Description: Comprehensive program using tuples to store and process fixed student information respecting immutability.

# Part 1: Declare original tuple
courses = (
    "Python",
    "Database",
    "Networking",
    "AI Fundamentals",
    "Web Development"
)
print("ORIGINAL COURSES")
print(courses)

# Part 2: Access tuple elements
print()
print("ACCESS ELEMENTS")
print("First course:", courses[0])
print("Last course:", courses[-1])

# Part 3: Tuple slicing
print()
print("TUPLE SLICING")
print("Selected courses (1 to 3):", courses[1:4])

# Part 4: Tuple length
print()
print("TUPLE LENGTH")
print("Number of courses:", len(courses))

# Part 5: Tuple methods
course_data = (
    "Python",
    "Database",
    "Python",
    "AI Fundamentals",
    "Python"
)
print()
print("TUPLE METHODS")
print("Python count:", course_data.count("Python"))
print("Database index:", course_data.index("Database"))

# Part 6: Membership testing
print()
print("MEMBERSHIP")
print("Python in courses:", "Python" in courses)
print("Java not in courses:", "Java" not in courses)

# Part 7: Modify using list conversion
print()
print("MODIFY THROUGH LIST CONVERSION")
course_list = list(courses)
course_list[1] = "SQL Database"
courses = tuple(course_list)
print("Updated tuple:", courses)

# Part 8: Add item by creating a new tuple
courses = courses + ("Machine Learning",)
print()
print("AFTER ADDING ITEM")
print(courses)

# Part 9: Combine tuples
additional_courses = ("Data Science", "Cloud Computing")
courses = courses + additional_courses
print()
print("FINAL COURSES")
print(courses)

'''
Sample Output:
ORIGINAL COURSES
('Python', 'Database', 'Networking', 'AI Fundamentals', 'Web Development')

ACCESS ELEMENTS
First course: Python
Last course: Web Development

TUPLE SLICING
Selected courses (1 to 3): ('Database', 'Networking', 'AI Fundamentals')

TUPLE LENGTH
Number of courses: 5

TUPLE METHODS
Python count: 3
Database index: 1

MEMBERSHIP
Python in courses: True
Java not in courses: True

MODIFY THROUGH LIST CONVERSION
Updated tuple: ('Python', 'SQL Database', 'Networking', 'AI Fundamentals', 'Web Development')

AFTER ADDING ITEM
('Python', 'SQL Database', 'Networking', 'AI Fundamentals', 'Web Development', 'Machine Learning')

FINAL COURSES
('Python', 'SQL Database', 'Networking', 'AI Fundamentals', 'Web Development', 'Machine Learning', 'Data Science', 'Cloud Computing')
'''
