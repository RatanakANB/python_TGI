# Worksheet No. 4.1: Python String Handling Practice Worksheet
# Description: Practice worksheet evaluating Python strings, indexing, slicing, length, methods, search, concatenation, format, and escape characters.

# Part A — Identify Strings
print("--- Part A: Identify Strings ---")
print('"Python" -> String? Yes')
print('20       -> String? No')
print("'Dara'   -> String? Yes")
print('85.5     -> String? No')
print('"20"     -> String? Yes')
print('True     -> String? No')

# Part B — Indexing
print("\n--- Part B: Indexing ---")
word = "Python"
print("word[0]  =", word[0])
print("word[1]  =", word[1])
print("word[2]  =", word[2])
print("word[5]  =", word[5])
print("word[-1] =", word[-1])
print("word[-2] =", word[-2])

# Part C — Slicing
print("\n--- Part C: Slicing ---")
course = "Python Programming"
print("course[0:6]  =", course[0:6])
print("course[:6]   =", course[:6])
print("course[7:]   =", course[7:])
print("course[-11:] =", course[-11:])

# Part D — String Length
print("\n--- Part D: String Length ---")
print('len("Python")      =', len("Python"))
print('len("Hello")       =', len("Hello"))
print('len("Hello World") =', len("Hello World"))

# Part E — String Methods
print("\n--- Part E: String Methods ---")
text = "Python Programming"
print("text.upper()                =", text.upper())
print("text.lower()                =", text.lower())
print("text.title()                =", text.title())
print('text.replace("Python", "AI") =', text.replace("Python", "AI"))
print('text.find("Python")         =', text.find("Python"))

# Part F — Search
print("\n--- Part F: Search ---")
print('"Python" in course   =', "Python" in course)
print('"Java" in course     =', "Java" in course)
print('"P" in course        =', "P" in course)
print('"Java" not in course =', "Java" not in course)

# Part G — Concatenation
print("\n--- Part G: Concatenation ---")
s = "favo"
t = "rite"
favorite = s + t
print("favorite =", favorite)

# Part H — format()
print("\n--- Part H: format() ---")
name = "Dara"
course_h = "Python"
result_h = "{} studies {}.".format(name, course_h)
print("Result:", result_h)

# Part I — Escape Characters
print("\n--- Part I: Escape Characters ---")
print("New line               : \\n")
print("Tab                    : \\t")
print("Backslash              : \\\\")
print('Double quotation mark  : \\"')

'''
Sample Output:
--- Part A: Identify Strings ---
"Python" -> String? Yes
20       -> String? No
'Dara'   -> String? Yes
85.5     -> String? No
"20"     -> String? Yes
True     -> String? No

--- Part B: Indexing ---
word[0]  = P
word[1]  = y
word[2]  = t
word[5]  = n
word[-1] = n
word[-2] = o

--- Part C: Slicing ---
course[0:6]  = Python
course[:6]   = Python
course[7:]   = Programming
course[-11:] = Programming

--- Part D: String Length ---
len("Python")      = 6
len("Hello")       = 5
len("Hello World") = 11

--- Part E: String Methods ---
text.upper()                = PYTHON PROGRAMMING
text.lower()                = python programming
text.title()                = Python Programming
text.replace("Python", "AI") = AI Programming
text.find("Python")         = 0

--- Part F: Search ---
"Python" in course   = True
"Java" in course     = False
"P" in course        = True
"Java" not in course = True

--- Part G: Concatenation ---
favorite = favorite

--- Part H: format() ---
Result: Dara studies Python.

--- Part I: Escape Characters ---
New line               : \n
Tab                    : \t
Backslash              : \\
Double quotation mark  : \"
'''
