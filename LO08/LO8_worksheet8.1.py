# Worksheet No. 8.1: Python Sets Practice
# Description: Practice worksheet evaluating Python sets concepts, modification, and operations.

print("--- Part A: Identify the Concept ---")
print("Collection storing unique values                  : Set")
print("Function used to create an empty set              : set()")
print("Method used to add one item                       : add()")
print("Method used to remove safely if item may be absent: discard()")
print("Operation returning common values                 : intersection()")
print("Built-in function used to count set elements      : len()")

print()
print("--- Part B: Complete the Code ---")
fruits = {"apple", "banana", "orange"}
fruits.add("mango")
fruits.discard("banana")
for fruit in sorted(fruits):
    print(fruit)

print()
print("--- Part C: Record the Set Operation Results ---")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("A.union(B)                :", A.union(B))
print("A.intersection(B)         :", A.intersection(B))
print("A.difference(B)           :", A.difference(B))
print("A.symmetric_difference(B) :", A.symmetric_difference(B))

'''
Sample Output:
--- Part A: Identify the Concept ---
Collection storing unique values                  : Set
Function used to create an empty set              : set()
Method used to add one item                       : add()
Method used to remove safely if item may be absent: discard()
Operation returning common values                 : intersection()
Built-in function used to count set elements      : len()

--- Part B: Complete the Code ---
apple
mango
orange

--- Part C: Record the Set Operation Results ---
A.union(B)                : {1, 2, 3, 4, 5, 6}
A.intersection(B)         : {3, 4}
A.difference(B)           : {1, 2}
A.symmetric_difference(B) : {1, 2, 5, 6}
'''
