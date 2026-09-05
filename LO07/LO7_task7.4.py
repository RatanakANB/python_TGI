# Task Sheet No. 7.4: Modify Tuple Data Using Conversion
# Description: Modify an immutable tuple item by converting to a list and back to a tuple.

courses = ("Python", "Database", "C#")
print("Original tuple:", courses)

# Convert to list
course_list = list(courses)

# Modify item in list
course_list[1] = "Machine Learning"

# Convert list back to tuple
courses = tuple(course_list)
print("Modified tuple:", courses)

'''
Sample Output:
Original tuple: ('Python', 'Database', 'C#')
Modified tuple: ('Python', 'Machine Learning', 'C#')
'''
