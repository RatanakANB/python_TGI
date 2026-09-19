# Task Sheet No. 11.6: Implement Lambda Functions
# Description: Anonymous single-line lambda functions for quick expressions.

# Practical Exercise A — Square
square = lambda number: number * number
print("Square of 5 :", square(5))

# Practical Exercise B — Addition
add = lambda a, b: a + b
print("add(5, 10)  :", add(5, 10))

# Practical Exercise C — Pass/Fail Status
status = lambda score: "Pass" if score >= 50 else "Fail"
print("Score 80    :", status(80))
print("Score 40    :", status(40))

'''
Sample Output:
Square of 5 : 25
add(5, 10)  : 15
Score 80    : Pass
Score 40    : Fail
'''
