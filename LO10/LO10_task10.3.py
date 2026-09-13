# Task Sheet No. 10.3: Process List Data Using for Loops
# Description: Iterate through student scores, evaluate pass/fail, and calculate totals.

scores = [75, 82, 45, 90, 68]
total = 0

for score in scores:
    print("Score:", score)
    if score >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")
    total += score

print()
print("Total:", total)

'''
Sample Output:
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

Total: 360
'''
