# Operation Sheet No. 5.1: Create and Execute Python Conditional Statements
# Program: control_flow.py
# Description: Demonstrates basic Python decision-making with if, elif, else, and logical conditions.

# Step 1: Initialize variables
a = 5
b = 10

# Step 2: Basic if statement
if b > a:
    print("b is greater than a")

# Step 3: if-elif-else structure
if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a and b are equal")

# Step 4: Testing multiple conditions with logical operators
if a < b and b == 10:
    print("Both conditions are true")

'''
Sample Output:
b is greater than a
b is greater than a
Both conditions are true
'''
