# Task Sheet No. 10.4: Apply break and continue in for Loops
# Description: Control for loop iterations using break and continue.

# Practical Exercise A — break
print("Practical Exercise A — break at 6:")
for number in range(1, 11):
    if number == 6:
        break
    print(number, end=" ")
print()

# Practical Exercise B — continue (skip even numbers)
print()
print("Practical Exercise B — continue (odd numbers only):")
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number, end=" ")
print()

'''
Sample Output:
Practical Exercise A — break at 6:
1 2 3 4 5 

Practical Exercise B — continue (odd numbers only):
1 3 5 7 9 
'''
