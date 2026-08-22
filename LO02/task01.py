# Task Sheet 2.3: Identify and Correct Python Errors

# Exercise 1 — Syntax Error (Fixed: added closing parenthesis)
name = "Dara"
print(name)

# Exercise 2 — Runtime Error (Fixed: avoid division by zero)
number = 20
divisor = 2  # Corrected from 0 to prevent ZeroDivisionError
result = number / divisor
print("Division result:", result)

# Exercise 3 — Logical Error (Fixed: use multiplication instead of addition)
length = 10
width = 5
area = length * width  # Corrected formula: length * width
print("Area:", area)

'''
Sample Output:
Dara
Division result: 10.0
Area: 50
'''
