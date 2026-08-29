# Worksheet No. 5.1: Python Control Flow Practice and Verification Worksheet
# Description: Practice worksheet evaluating comparison operators, logical operators, and conditionals.

print("--- Part A: Comparison Operators ---")
print("== : Equal to")
print("!= : Not equal to")
print(">  : Greater than")
print("<  : Less than")
print(">= : Greater than or equal to")
print("<= : Less than or equal to")

print("\n--- Part B: Logical Operators ---")
print("and : Returns True if both statements are true")
print("or  : Returns True if one of the statements is true")
print("not : Reverse the result, returns False if the result is true")

print("\n--- Part C: Evaluate Conditions ---")
a = 5
b = 10
print("b > a               :", b > a)
print("a > b               :", a > b)
print("a == b              :", a == b)
print("a != b              :", a != b)
print("a < b and b == 10   :", a < b and b == 10)
print("a > b or b == 10    :", a > b or b == 10)
print("not a > b           :", not a > b)

print("\n--- Part D: Complete if Statement ---")
if b > a:
    print("b is greater than a")

print("\n--- Part E: Complete if-else ---")
score = 45
if score >= 50:
    print("Pass")
else:
    print("Fail")

print("\n--- Part F: Complete if-elif-else ---")
score = 75
if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
else:
    print("Grade C")

print("\n--- Part G: Shorthand Conditional Expression ---")
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

print("\n--- Part H: Flowchart Symbols ---")
print("Start/End        : Oval (Rounded Rectangle)")
print("Process          : Rectangle")
print("Decision         : Diamond")
print("Input/Output     : Parallelogram")
print("Direction of flow: Arrow")

'''
Sample Output:
--- Part A: Comparison Operators ---
== : Equal to
!= : Not equal to
>  : Greater than
<  : Less than
>= : Greater than or equal to
<= : Less than or equal to

--- Part B: Logical Operators ---
and : Returns True if both statements are true
or  : Returns True if one of the statements is true
not : Reverse the result, returns False if the result is true

--- Part C: Evaluate Conditions ---
b > a               : True
a > b               : False
a == b              : False
a != b              : True
a < b and b == 10   : True
a > b or b == 10    : True
not a > b           : True

--- Part D: Complete if Statement ---
b is greater than a

--- Part E: Complete if-else ---
Fail

--- Part F: Complete if-elif-else ---
Grade B

--- Part G: Shorthand Conditional Expression ---
Status: Adult

--- Part H: Flowchart Symbols ---
Start/End        : Oval (Rounded Rectangle)
Process          : Rectangle
Decision         : Diamond
Input/Output     : Parallelogram
Direction of flow: Arrow
'''
