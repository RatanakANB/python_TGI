# Task Sheet No. 12.2: Define and Use Class Attributes and Methods
# Description: Expand class with behaviors, display methods, and attribute mutations.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_info(self):
        print("Name  :", self.name)
        print("Score :", self.score)

    def get_result(self):
        return "Pass" if self.score >= 50 else "Fail"

student1 = Student("Dara", 85)
student1.display_info()
print("Result:", student1.get_result())

# Modify attribute
print()
student1.score = 95
print("After updating score:")
student1.display_info()
print("Result:", student1.get_result())

'''
Sample Output:
Name  : Dara
Score : 85
Result: Pass

After updating score:
Name  : Dara
Score : 95
Result: Pass
'''
