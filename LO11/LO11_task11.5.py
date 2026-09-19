# Task Sheet No. 11.5: Implement Recursive Functions
# Description: Define recursive functions with base cases for problem reduction.

# Practical Exercise A — Countdown
print("Countdown:")
def countdown(number):
    if number <= 0:
        print("Done")
        return
    print(number)
    countdown(number - 1)

countdown(5)

# Practical Exercise B — Factorial
print()
def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print("Factorial of 5:", factorial(5))

'''
Sample Output:
Countdown:
5
4
3
2
1
Done

Factorial of 5: 120
'''
