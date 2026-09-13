# Worksheet No. 10.1: Python Loop Structure Practice and Verification Worksheet
# Description: Practice worksheet evaluating Python while loops, for loops, range, and nested loops.

# Part A — Identify Loop Components
print("--- Part A: Identify Loop Components ---")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
print("Final count after loop:", count)

# Part B — range() Outputs
print()
print("--- Part B: range() Outputs ---")
print("list(range(5))        =", list(range(5)))
print("list(range(1, 6))     =", list(range(1, 6)))
print("list(range(2, 11, 2)) =", list(range(2, 11, 2)))
print("list(range(5, 0, -1)) =", list(range(5, 0, -1)))

# Part C — break and continue
print()
print("--- Part C: break and continue ---")
print("break demo    :", [i for i in range(1, 10) if i < 5])
print("continue demo :", [i for i in range(1, 6) if i != 3])

# Part D — Nested Loop Count
print()
print("--- Part D: Nested Loop Count ---")
iterations = 0
for r in range(3):
    for c in range(4):
        iterations += 1
print("Total inner loop iterations (3 rows x 4 cols) =", iterations)

'''
Sample Output:
--- Part A: Identify Loop Components ---
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
Final count after loop: 6

--- Part B: range() Outputs ---
list(range(5))        = [0, 1, 2, 3, 4]
list(range(1, 6))     = [1, 2, 3, 4, 5]
list(range(2, 11, 2)) = [2, 4, 6, 8, 10]
list(range(5, 0, -1)) = [5, 4, 3, 2, 1]

--- Part C: break and continue ---
break demo    : [1, 2, 3, 4]
continue demo : [1, 2, 4, 5]

--- Part D: Nested Loop Count ---
Total inner loop iterations (3 rows x 4 cols) = 12
'''
