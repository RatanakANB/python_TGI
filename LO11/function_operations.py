# Operation Sheet No. 11.1: Create and Execute Python Functions
# Program: function_operations.py
# Description: Demonstrates standard procedures for creating, calling, and executing Python functions.

# Step 1: Basic function
def greet():
    print("Hello Python")

greet()

# Step 2: Function with arguments
def student_info(name, age):
    print("Student:", name, "| Age:", age)

student_info("Dara", 20)

# Step 3: Pass a list to a function
def display_scores(scores):
    for score in scores:
        print("Score:", score)

display_scores([80, 90, 75])

# Step 4: Return statement
def add(a, b):
    return a + b

print("Sum:", add(5, 10))

# Step 5: Default parameter
def welcome(name="Student"):
    print("Welcome,", name)

welcome()
welcome("Dara")

# Step 6: Arbitrary arguments (*args and **kwargs)
def total(*numbers):
    return sum(numbers)

print("Total with *args:", total(10, 20, 30))

def profile_data(**data):
    print("Profile with **kwargs:", data)

profile_data(name="Dara", course="Python")

# Step 7: Lambda function
square = lambda x: x * x
print("Lambda square(5):", square(5))

'''
Sample Output:
Hello Python
Student: Dara | Age: 20
Score: 80
Score: 90
Score: 75
Sum: 15
Welcome, Student
Welcome, Dara
Total with *args: 60
Profile with **kwargs: {'name': 'Dara', 'course': 'Python'}
Lambda square(5): 25
'''
