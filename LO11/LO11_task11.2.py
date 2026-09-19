# Task Sheet No. 11.2: Pass Values and Lists to Functions
# Description: Pass positional arguments and collection data to Python functions.

# Exercise A: Positional parameters
def show_student(name, age):
    print("Name:", name)
    print("Age :", age)

print("Individual values:")
show_student("Dara", 20)

# Exercise B: Passing a list
def display_scores(scores):
    for score in scores:
        print("Score:", score)

print()
print("List processing in function:")
display_scores([80, 85, 90])

'''
Sample Output:
Individual values:
Name: Dara
Age : 20

List processing in function:
Score: 80
Score: 85
Score: 90
'''
