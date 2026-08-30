# Worksheet No. 6.1: Python List Practice and Verification Worksheet
# Description: Practice worksheet evaluating Python lists, indexing, slicing, modification, and methods.

# Part A — List Declaration
languages = ["Python", "Java", "C++", "JavaScript", "PHP"]
print("--- Part A: List Declaration ---")
print("languages =", languages)

# Part B — Indexing
fruits = ["apple", "banana", "orange", "mango", "grape"]
print("\n--- Part B: Indexing ---")
print("fruits[0]  =", fruits[0])
print("fruits[2]  =", fruits[2])
print("fruits[-1] =", fruits[-1])
print("fruits[-2] =", fruits[-2])

# Part C — Slicing
numbers = [10, 20, 30, 40, 50, 60]
print("\n--- Part C: Slicing ---")
print("numbers[1:4] =", numbers[1:4])
print("numbers[:3]  =", numbers[:3])
print("numbers[3:]  =", numbers[3:])
print("numbers[-3:] =", numbers[-3:])

# Part D — Modify List
colors = ["red", "green", "blue"]
colors[1] = "yellow"
print("\n--- Part D: Modify List ---")
print("colors =", colors)

# Part E — List Length
scores = [80, 75, 90, 85, 70]
print("\n--- Part E: List Length ---")
print("Number of scores =", len(scores))

# Part F — Add Items
students = ["Dara", "Sokha"]
students.append("Vanna")
students.insert(1, "Malis")
print("\n--- Part F: Add Items ---")
print("students =", students)

# Part G — Remove Items
items = ["pencil", "ruler", "eraser", "book"]
items.remove("ruler")
popped = items.pop()
print("\n--- Part G: Remove Items ---")
print("Remaining items =", items)
print("Popped item     =", popped)

'''
Sample Output:
--- Part A: List Declaration ---
languages = ['Python', 'Java', 'C++', 'JavaScript', 'PHP']

--- Part B: Indexing ---
fruits[0]  = apple
fruits[2]  = orange
fruits[-1] = grape
fruits[-2] = mango

--- Part C: Slicing ---
numbers[1:4] = [20, 30, 40]
numbers[:3]  = [10, 20, 30]
numbers[3:]  = [40, 50, 60]
numbers[-3:] = [40, 50, 60]

--- Part D: Modify List ---
colors = ['red', 'yellow', 'blue']

--- Part E: List Length ---
Number of scores = 5

--- Part F: Add Items ---
students = ['Dara', 'Malis', 'Sokha', 'Vanna']

--- Part G: Remove Items ---
Remaining items = ['pencil', 'eraser']
Popped item     = book
'''
