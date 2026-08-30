# Job Sheet No. 6.1: Develop a Student Score Management Program Using Lists
# Program: student_score_manager.py
# Description: Complete Python program that uses lists to store and manage student scores.

# 1. Declare list with student scores
scores = [75, 85, 90, 65, 80]
print("STUDENT SCORE MANAGEMENT")
print("Original scores:", scores)

# 2. Access elements using positive and negative indexing
print("First score:", scores[0])
print("Last score:", scores[-1])

# 3. List slicing
print("Scores from index 1 to 3:", scores[1:4])

# 4. Change a score
scores[3] = 70
print("After update:", scores)

# 5. Determine list length
print("Number of scores:", len(scores))

# 6. Add elements (append and insert)
scores.append(95)
print("After append:", scores)
scores.insert(2, 88)
print("After insert:", scores)

# 7. Remove elements (remove and pop)
scores.remove(75)
print("After remove:", scores)
removed_score = scores.pop()
print("Popped score:", removed_score)

# 8. Sort scores
scores.sort()
print("Sorted scores:", scores)

# 9. Lowest and highest after sorting
print("Lowest score:", scores[0])
print("Highest score:", scores[-1])

# 10. Count and index methods
print("Number of 85 scores:", scores.count(85))
print("Index of 90:", scores.index(90))
print("Final scores:", scores)

'''
Sample Output:
STUDENT SCORE MANAGEMENT
Original scores: [75, 85, 90, 65, 80]
First score: 75
Last score: 80
Scores from index 1 to 3: [85, 90, 65]
After update: [75, 85, 90, 70, 80]
Number of scores: 5
After append: [75, 85, 90, 70, 80, 95]
After insert: [75, 85, 88, 90, 70, 80, 95]
After remove: [85, 88, 90, 70, 80, 95]
Popped score: 95
Sorted scores: [70, 80, 85, 88, 90]
Lowest score: 70
Highest score: 90
Number of 85 scores: 1
Index of 90: 4
Final scores: [70, 80, 85, 88, 90]
'''
