# Task Sheet No. 6.4: Remove and Organize List Elements
# Description: Remove, sort, reverse and inspect list elements using built-in methods.

scores = [80, 70, 90, 60, 70, 85]
print("Original scores:", scores)

# remove()
scores.remove(60)
print("After remove(60):", scores)

# pop()
removed_score = scores.pop(0)
print("Removed with pop(0):", removed_score)
print("Scores after pop:", scores)

# sort()
scores.sort()
print("Sorted scores:", scores)

# reverse()
scores.reverse()
print("Reversed scores:", scores)

# count()
print("Count of 70:", scores.count(70))

# index()
print("Index of 90:", scores.index(90))

'''
Sample Output:
Original scores: [80, 70, 90, 60, 70, 85]
After remove(60): [80, 70, 90, 70, 85]
Removed with pop(0): 80
Scores after pop: [70, 90, 70, 85]
Sorted scores: [70, 70, 85, 90]
Reversed scores: [90, 85, 70, 70]
Count of 70: 2
Index of 90: 0
'''
