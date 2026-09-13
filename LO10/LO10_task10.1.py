# Task Sheet No. 10.1: Apply break, continue, and while-else
# Description: Control while loop execution using break, continue, and else clauses.

# Exercise A — break
print("Exercise A — break:")
count = 1
while count <= 10:
    if count == 6:
        break
    print(count)
    count += 1

# Exercise B — continue
print()
print("Exercise B — continue:")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

# Exercise C — while-else
print()
print("Exercise C — while-else:")
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Completed")

'''
Sample Output:
Exercise A — break:
1
2
3
4
5

Exercise B — continue:
1
2
4
5

Exercise C — while-else:
1
2
3
Completed
'''
