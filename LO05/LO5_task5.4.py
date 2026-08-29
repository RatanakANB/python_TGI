# Task Sheet No. 5.4: Apply Shorthand and Nested Conditional Statements
# Description: Develop shorthand and nested Python conditional statements

# Practical Exercise A — Shorthand if
a = 5
b = 10
if b > a: print("b is greater than a")

# Practical Exercise B — Conditional Expression (Ternary Operator)
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# Practical Exercise C — Nested if
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry denied")

'''
Sample Output:
b is greater than a
Status: Adult
Entry allowed
'''
