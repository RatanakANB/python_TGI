# Job Sheet No. 5.1: Develop a Student Result Decision Program
# Program: student_result_decision.py
# Description: Comprehensive control flow program evaluating student results, grade, pass/fail status, and eligibility.

# Part 1 — Variables
student_name = "Dara"
score = 85
attendance = 90

print("STUDENT RESULT")
print("Name:", student_name)
print("Score:", score)
print("Attendance:", attendance)

# Part 2 — Determine grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)

# Part 3 & 4 — Determine pass/fail and nested condition
if score >= 60 and attendance >= 75:
    print("Result: Pass")
    # Nested condition
    if score >= 90:
        print("Performance: Excellent")
    else:
        print("Performance: Satisfactory")
else:
    print("Result: Fail")

# Part 5 — Shorthand conditional expression
eligibility = "Eligible" if attendance >= 75 else "Not Eligible"
print("Eligibility:", eligibility)

'''
Sample Output:
STUDENT RESULT
Name: Dara
Score: 85
Attendance: 90
Grade: B
Result: Pass
Performance: Satisfactory
Eligibility: Eligible
'''
