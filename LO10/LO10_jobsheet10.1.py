# Job Sheet No. 10.1: Develop a Student Score Processing Program Using Loop Structures
# Program: student_score_processing.py
# Description: Comprehensive loop program evaluating while, for, range, break, continue, else, and nested loops.

print("================================")
print("       LOOP DEMONSTRATION")
print("================================")

# 1. Basic while loop
print()
print("WHILE LOOP")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
else:
    print("While loop completed")

# 2. break
print()
print("BREAK EXAMPLE")
number = 1
while number <= 10:
    if number == 6:
        print("Break at:", number)
        break
    print(number)
    number += 1

# 3. continue
print()
print("CONTINUE EXAMPLE")
number = 0
while number < 5:
    number += 1
    if number == 3:
        continue
    print(number)

# 4. for loop and range()
print()
print("FOR LOOP WITH RANGE")
for number in range(1, 6):
    print(number)

# 5. Student score processing
print()
print("STUDENT SCORE PROCESSING")
scores = [75, 82, 45, 90, 68]
total = 0
pass_count = 0
for score in scores:
    print("Score:", score)
    if score >= 50:
        print("Result: Pass")
        pass_count += 1
    else:
        print("Result: Fail")
    total += score

print("Total Score:", total)
print("Pass Count:", pass_count)

# 6. Nested loop: multiplication table
print()
print("MULTIPLICATION TABLE")
for row in range(1, 4):
    for column in range(1, 6):
        print(f"{row} x {column} = {row * column}")
    print()

'''
Sample Output:
================================
       LOOP DEMONSTRATION
================================

WHILE LOOP
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
While loop completed

BREAK EXAMPLE
1
2
3
4
5
Break at: 6

CONTINUE EXAMPLE
1
2
4
5

FOR LOOP WITH RANGE
1
2
3
4
5

STUDENT SCORE PROCESSING
Score: 75
Result: Pass
Score: 82
Result: Pass
Score: 45
Result: Fail
Score: 90
Result: Pass
Score: 68
Result: Pass
Total Score: 360
Pass Count: 4

MULTIPLICATION TABLE
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15

'''
