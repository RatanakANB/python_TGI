# Operation Sheet No. 7.1: Create, Access, and Manipulate Python Tuples
# Program: tuple_operations.py
# Description: Demonstrates standard procedures for working with Python tuples while respecting immutability.

# Step 1: Create tuple
fruits = ("apple", "banana", "orange", "mango")
print("Original tuple:", fruits)

# Step 2: Access elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Step 3: Slice tuple
print("Sliced (index 1 to 3):", fruits[1:3])

# Step 4: Determine length
print("Tuple length:", len(fruits))

# Step 5: Tuple methods
data = (10, 20, 10, 30, 10)
print("Count of 10:", data.count(10))
print("Index of 20:", data.index(20))

# Step 6: Modify through list conversion
temp_list = list(fruits)
temp_list[1] = "grape"
fruits = tuple(temp_list)
print("After conversion modification:", fruits)

# Step 7: Add an item by creating a new tuple
fruits = fruits + ("watermelon",)
print("After adding item:", fruits)

'''
Sample Output:
Original tuple: ('apple', 'banana', 'orange', 'mango')
First fruit: apple
Last fruit: mango
Sliced (index 1 to 3): ('banana', 'orange')
Tuple length: 4
Count of 10: 3
Index of 20: 1
After conversion modification: ('apple', 'grape', 'orange', 'mango')
After adding item: ('apple', 'grape', 'orange', 'mango', 'watermelon')
'''
