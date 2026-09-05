# Task Sheet No. 7.5: Add and Combine Tuple Items
# Description: Add items to tuples using concatenation and combine multiple tuples.

# Practical Exercise A — Add One Item
languages = ("Python", "C#")
languages = languages + ("Java",)
print("After adding one item:", languages)

# Practical Exercise B — Combine Tuples
frontend = ("HTML", "CSS")
backend = ("Python", "SQL")
technologies = frontend + backend
print("Combined technologies:", technologies)

'''
Sample Output:
After adding one item: ('Python', 'C#', 'Java')
Combined technologies: ('HTML', 'CSS', 'Python', 'SQL')
'''
