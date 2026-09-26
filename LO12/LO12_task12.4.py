# Task Sheet No. 12.4: Import and Use Built-In Python Modules
# Description: Import and apply standard library modules math and random with aliases.

import math
from math import sqrt
import math as m
import random

# Math operations
print("math.sqrt(25) :", math.sqrt(25))
print("math.pi       :", round(math.pi, 4))
print("sqrt(81)      :", sqrt(81))
print("m.pow(2, 3)   :", m.pow(2, 3))

# Random operation
random.seed(42)
print("random.randint(1, 100):", random.randint(1, 100))

'''
Sample Output:
math.sqrt(25) : 5.0
math.pi       : 3.1416
sqrt(81)      : 9.0
m.pow(2, 3)   : 8.0
random.randint(1, 100): 82
'''
