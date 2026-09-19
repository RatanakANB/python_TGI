# Worksheet No. 11.1: Python Function Practice and Verification Worksheet
# Description: Practice worksheet evaluating Python function declarations, parameters, return, args/kwargs, and lambda.

# Part A — Function Structure
def greet():
    print("Hello")

print("--- Part A: Function Structure ---")
greet()

# Part B — Parameters and Arguments
def add_numbers(x, y=10):
    return x + y

print()
print("--- Part B: Parameters and Arguments ---")
print("add_numbers(5)    =", add_numbers(5))
print("add_numbers(5, 7) =", add_numbers(5, 7))

# Part C — *args and **kwargs
def process_data(*args, **kwargs):
    return sum(args), kwargs

total, info = process_data(1, 2, 3, course="Python")
print()
print("--- Part C: *args and **kwargs ---")
print("Total from *args   =", total)
print("Dictionary **kwargs =", info)

# Part D — Lambda and Recursion
mult = lambda a, b: a * b
print()
print("--- Part D: Lambda and Recursion ---")
print("Lambda mult(4, 5)  =", mult(4, 5))

def sum_to_n(n):
    if n <= 1:
        return n
    return n + sum_to_n(n - 1)

print("Recursive sum to 5 =", sum_to_n(5))

'''
Sample Output:
--- Part A: Function Structure ---
Hello

--- Part B: Parameters and Arguments ---
add_numbers(5)    = 15
add_numbers(5, 7) = 12

--- Part C: *args and **kwargs ---
Total from *args   = 6
Dictionary **kwargs = {'course': 'Python'}

--- Part D: Lambda and Recursion ---
Lambda mult(4, 5)  = 20
Recursive sum to 5 = 15
'''
