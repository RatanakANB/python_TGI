# Job Sheet No. 11.1: Develop a Student Result Processing Program Using Functions
# Program: student_result_processing.py
# Description: Modular student management program using comprehensive Python function techniques.

# 1. Default argument function
def display_student(name, course="Python"):
    print("Name   :", name)
    print("Course :", course)

print("STUDENT INFORMATION")
display_student("Dara")

# 2. Return function with list
def calculate_total(scores):
    total = 0
    for score in scores:
        total += score
    return total

def calculate_average(scores):
    total = calculate_total(scores)
    return total / len(scores)

scores = [80, 85, 90]
total = calculate_total(scores)
average = calculate_average(scores)
print()
print("ACADEMIC PERFORMANCE")
print("Scores  :", scores)
print("Total   :", total)
print("Average :", average)

# 3. Arbitrary positional arguments (*args)
def score_total(*scores):
    return sum(scores)

print("Arbitrary total (80, 85, 90):", score_total(80, 85, 90))

# 4. Arbitrary keyword arguments (**kwargs)
print()
def show_profile(**student):
    print("Student Profile:")
    for key, value in student.items():
        print(f"  {key}: {value}")

show_profile(id="ST001", name="Dara", level="II")

# 5. Placeholder function using pass
def export_report():
    pass

export_report()

# 6. Recursive function
def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print()
print("Recursive factorial(5):", factorial(5))

# 7. Lambda function
result_status = lambda score: "Pass" if score >= 50 else "Fail"
print("Status for score 85  :", result_status(85))

'''
Sample Output:
STUDENT INFORMATION
Name   : Dara
Course : Python

ACADEMIC PERFORMANCE
Scores  : [80, 85, 90]
Total   : 255
Average : 85.0
Arbitrary total (80, 85, 90): 255

Student Profile:
  id: ST001
  name: Dara
  level: II

Recursive factorial(5): 120
Status for score 85  : Pass
'''
