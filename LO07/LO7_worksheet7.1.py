# Worksheet No. 7.1: Python Tuple Practice and Verification Worksheet
# Description: Practice worksheet evaluating Python tuples, indexing, slicing, methods, conversion, and concatenation.

# Part A — Tuple Declaration
languages = ("Python", "Java", "C++", "JavaScript", "PHP")
print("--- Part A: Tuple Declaration ---")
print("languages =", languages)

# Part B — One-Item Tuple
single_item = ("Python",)
print()
print("--- Part B: One-Item Tuple ---")
print("single_item =", single_item)
print("type        =", type(single_item).__name__)

# Part C — Positive Indexing
fruits = ("apple", "banana", "orange", "mango", "grape")
print()
print("--- Part C: Positive Indexing ---")
print("fruits[0] =", fruits[0])
print("fruits[1] =", fruits[1])
print("fruits[3] =", fruits[3])

# Part D — Negative Indexing
print()
print("--- Part D: Negative Indexing ---")
print("fruits[-1] =", fruits[-1])
print("fruits[-2] =", fruits[-2])
print("fruits[-3] =", fruits[-3])

# Part E — Slicing
numbers = (10, 20, 30, 40, 50, 60)
print()
print("--- Part E: Slicing ---")
print("numbers[1:4] =", numbers[1:4])
print("numbers[:3]  =", numbers[:3])
print("numbers[3:]  =", numbers[3:])
print("numbers[-3:] =", numbers[-3:])

# Part F — Tuple Length
scores = (80, 75, 90, 85, 70)
print()
print("--- Part F: Tuple Length ---")
print("Number of elements =", len(scores))

# Part G — Methods
scores_data = (80, 90, 80, 70, 80)
print()
print("--- Part G: Methods ---")
print("scores_data.count(80) =", scores_data.count(80))
print("scores_data.index(90) =", scores_data.index(90))

# Part H — Modification via Conversion
t = ("red", "green", "blue")
lst = list(t)
lst[1] = "yellow"
t = tuple(lst)
print()
print("--- Part H: Conversion Modification ---")
print("Modified tuple =", t)

'''
Sample Output:
--- Part A: Tuple Declaration ---
languages = ('Python', 'Java', 'C++', 'JavaScript', 'PHP')

--- Part B: One-Item Tuple ---
single_item = ('Python',)
type        = tuple

--- Part C: Positive Indexing ---
fruits[0] = apple
fruits[1] = banana
fruits[3] = mango

--- Part D: Negative Indexing ---
fruits[-1] = grape
fruits[-2] = mango
fruits[-3] = orange

--- Part E: Slicing ---
numbers[1:4] = (20, 30, 40)
numbers[:3]  = (10, 20, 30)
numbers[3:]  = (40, 50, 60)
numbers[-3:] = (40, 50, 60)

--- Part F: Tuple Length ---
Number of elements = 5

--- Part G: Methods ---
scores_data.count(80) = 3
scores_data.index(90) = 1

--- Part H: Conversion Modification ---
Modified tuple = ('red', 'yellow', 'blue')
'''
