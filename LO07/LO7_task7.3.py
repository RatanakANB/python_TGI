# Task Sheet No. 7.3: Apply Tuple Methods and Keywords
# Description: Apply count, index, in, and not in on tuple data.

languages = ("Python", "Java", "C#", "Python", "JavaScript", "Python")
print("Languages tuple:", languages)

print("Python count      :", languages.count("Python"))
print("Java index        :", languages.index("Java"))
print("'C#' in tuple     :", "C#" in languages)
print("'PHP' not in tuple:", "PHP" not in languages)

'''
Sample Output:
Languages tuple: ('Python', 'Java', 'C#', 'Python', 'JavaScript', 'Python')
Python count      : 3
Java index        : 1
'C#' in tuple     : True
'PHP' not in tuple: True
'''
