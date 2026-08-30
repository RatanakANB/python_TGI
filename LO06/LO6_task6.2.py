# Task Sheet No. 6.2: Apply List Slicing and Modify List Elements
# Description: Retrieve specified ranges of list elements and modify individual and multiple values.

numbers = [10, 20, 30, 40, 50, 60]
print("Original numbers:", numbers)

# Slicing operations
print("numbers[1:4]  :", numbers[1:4])
print("numbers[:3]   :", numbers[:3])
print("numbers[3:]   :", numbers[3:])
print("numbers[-3:]  :", numbers[-3:])

# Modify single element
numbers[2] = 35
print("After modifying index 2:", numbers)

# Modify multiple elements using slicing
numbers[0:2] = [15, 25]
print("After modifying slice 0:2:", numbers)

'''
Sample Output:
Original numbers: [10, 20, 30, 40, 50, 60]
numbers[1:4]  : [20, 30, 40]
numbers[:3]   : [10, 20, 30]
numbers[3:]   : [40, 50, 60]
numbers[-3:]  : [40, 50, 60]
After modifying index 2: [10, 20, 35, 40, 50, 60]
After modifying slice 0:2: [15, 25, 35, 40, 50, 60]
'''
