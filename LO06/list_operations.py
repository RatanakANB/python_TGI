# Operation Sheet No. 6.1: Create, Access, and Manipulate Python Lists
# Program: list_operations.py
# Description: Demonstrates standard procedures for creating and manipulating Python lists.

# Step 1: Create list
fruits = ["apple", "banana", "orange", "mango"]
print("Original list:", fruits)

# Step 2: Access elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Step 3: Slice the list
print("Sliced (index 1 to 3):", fruits[1:3])

# Step 4: Modify an item
fruits[1] = "grape"
print("After modification:", fruits)

# Step 5: Determine length
print("List length:", len(fruits))

# Step 6: Add items
fruits.append("watermelon")
print("After append:", fruits)

# Step 7: Remove items
fruits.remove("orange")
print("After remove:", fruits)

# Step 8: Sort list
fruits.sort()
print("Sorted list:", fruits)

'''
Sample Output:
Original list: ['apple', 'banana', 'orange', 'mango']
First fruit: apple
Last fruit: mango
Sliced (index 1 to 3): ['banana', 'orange']
After modification: ['apple', 'grape', 'orange', 'mango']
List length: 4
After append: ['apple', 'grape', 'orange', 'mango', 'watermelon']
After remove: ['apple', 'grape', 'mango', 'watermelon']
Sorted list: ['apple', 'grape', 'mango', 'watermelon']
'''
