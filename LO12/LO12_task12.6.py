# Task Sheet No. 12.6: Integrate Classes, Modules, and Packages
# Description: Combine OOP class instances, modular utility functions, and package architecture.

from school.student import Student
from school.utilities import calculate_total, calculate_average

student1 = Student("ST001", "Dara", "Python", [80, 90, 75])
student2 = Student("ST002", "Sokha", "Python", [88, 92, 94])

for st in [student1, student2]:
    print("--------------------")
    st.display_info()
    print("Total   :", calculate_total(st.scores))
    print("Average :", calculate_average(st.scores))
    print("Result  :", st.get_result())

'''
Sample Output:
--------------------
ID     : ST001
Name   : Dara
Course : Python
Scores : [80, 90, 75]
Total   : 245
Average : 81.66666666666667
Result  : Pass
--------------------
ID     : ST002
Name   : Sokha
Course : Python
Scores : [88, 92, 94]
Total   : 274
Average : 91.33333333333333
Result  : Pass
'''
