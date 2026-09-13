# Task Sheet No. 10.5: Develop Nested Loop Structures
# Description: Multi-level loop patterns and multiplication grid.

# Exercise A — Pattern
print("Exercise A — Pattern:")
for row in range(3):
    for column in range(4):
        print("*", end=" ")
    print()

# Exercise B — Multiplication Table
print()
print("Exercise B — Multiplication Table:")
for i in range(1, 4):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}", end="	")
    print()

'''
Sample Output:
Exercise A — Pattern:
* * * * 
* * * * 
* * * * 

Exercise B — Multiplication Table:
1 x 1 = 1	1 x 2 = 2	1 x 3 = 3	1 x 4 = 4	1 x 5 = 5	
2 x 1 = 2	2 x 2 = 4	2 x 3 = 6	2 x 4 = 8	2 x 5 = 10	
3 x 1 = 3	3 x 2 = 6	3 x 3 = 9	3 x 4 = 12	3 x 5 = 15	
'''
