# Operation Sheet No. 10.1: Create and Execute Python Loop Structures
# Program: loop_operations.py
# Description: Demonstrates standard procedures for developing repetitive Python loop programs.

# Step 1: Counter-controlled while loop with else
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed")

# Step 2: for loop with range
print()
print("for loop with range(1, 6):")
for number in range(1, 6):
    print(number)

# Step 3: Iterate through a list
print()
print("Iterate list of students:")
students = ["Dara", "Sokha", "Vanna"]
for student in students:
    print(student)

# Step 4: Nested loops
print()
print("Nested loop (row, col):")
for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row}, {column})", end=" ")
    print()

'''
Sample Output:
1
2
3
Loop completed

for loop with range(1, 6):
1
2
3
4
5

Iterate list of students:
Dara
Sokha
Vanna

Nested loop (row, col):
(1, 1) (1, 2) (1, 3) 
(2, 1) (2, 2) (2, 3) 
(3, 1) (3, 2) (3, 3) 
'''
