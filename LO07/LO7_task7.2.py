# Task Sheet No. 7.2: Apply Tuple Slicing and Built-in Functions
# Description: Retrieve specified tuple ranges and apply built-in functions len, min, max, sum.

scores = (70, 80, 90, 60, 85, 75)
print("Original scores:", scores)

# Slicing operations
print("scores[1:4]  :", scores[1:4])
print("scores[:3]   :", scores[:3])
print("scores[3:]   :", scores[3:])
print("scores[-3:]  :", scores[-3:])

# Built-in functions
print("Length :", len(scores))
print("Minimum:", min(scores))
print("Maximum:", max(scores))
print("Sum    :", sum(scores))

'''
Sample Output:
Original scores: (70, 80, 90, 60, 85, 75)
scores[1:4]  : (80, 90, 60)
scores[:3]   : (70, 80, 90)
scores[3:]   : (60, 85, 75)
scores[-3:]  : (60, 85, 75)
Length : 6
Minimum: 60
Maximum: 90
Sum    : 460
'''
