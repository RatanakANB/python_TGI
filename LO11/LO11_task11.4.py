# Task Sheet No. 11.4: Apply Arbitrary Arguments and pass
# Description: Variable-length *args, **kwargs, and empty placeholder functions using pass.

# Practical Exercise A — *args
def calculate_total(*scores):
    total = 0
    for score in scores:
        total += score
    return total

print("calculate_total(80, 90, 70) =", calculate_total(80, 90, 70))

# Practical Exercise B — **kwargs
print()
def student_profile(**student):
    print("Name   :", student.get("name"))
    print("Course :", student.get("course"))

student_profile(name="Dara", course="Python")

# Practical Exercise C — pass
def future_report():
    pass

future_report()
print("future_report() executed with pass statement successfully.")

'''
Sample Output:
calculate_total(80, 90, 70) = 240

Name   : Dara
Course : Python
future_report() executed with pass statement successfully.
'''
