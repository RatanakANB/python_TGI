# Task Sheet No. 5.3: Develop if-elif-else Decision Statements
# Description: Evaluate multiple conditions using if, elif, and else to classify scores

# Practical Exercise
score = 75

if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
else:
    print("Grade C")

# Testing different score cases
test_scores = [85, 75, 60]
for s in test_scores:
    if s >= 80:
        grade = "Grade A"
    elif s >= 70:
        grade = "Grade B"
    else:
        grade = "Grade C"
    print(f"Score: {s} -> {grade}")

'''
Sample Output:
Grade B
Score: 85 -> Grade A
Score: 75 -> Grade B
Score: 60 -> Grade C
'''
