# Task Sheet No. 8.2: Add and Remove Python Set Items
# Description: Practice modifying sets using add, update, remove, and discard methods.

fruits = {"apple", "banana", "cherry"}
print("Original fruits:", fruits)

# Add single item
fruits.add("mango")
print("After add('mango'):", fruits)

# Add multiple items with update()
fruits.update(["orange", "melon"])
print("After update(['orange', 'melon']):", fruits)

# Remove item with remove()
fruits.remove("banana")
print("After remove('banana'):", fruits)

# Discard item (does not raise error if absent)
fruits.discard("grape")
print("After discard('grape'):", fruits)

'''
Sample Output:
Original fruits: {'apple', 'cherry', 'banana'}
After add('mango'): {'apple', 'cherry', 'banana', 'mango'}
After update(['orange', 'melon']): {'apple', 'melon', 'orange', 'cherry', 'banana', 'mango'}
After remove('banana'): {'apple', 'melon', 'orange', 'cherry', 'mango'}
After discard('grape'): {'apple', 'melon', 'orange', 'cherry', 'mango'}
'''
