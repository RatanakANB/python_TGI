# Operation Sheet No. 8.1: Create, Process and Verify Python Sets
# Program: set_operations.py
# Description: Demonstrates standard procedures for creating, modifying, and applying set operations in Python.

# Step 1: Create sets
skills = {"Python", "Database", "Networking", "Python"}
print("Initial set (duplicates removed):", skills)

# Step 2: Access elements through iteration
print()
print("Iterating skills:")
for skill in skills:
    print("-", skill)

# Step 3: Add items
skills.add("Cloud")
skills.update(["AI", "Security"])
print()
print("After adding items:", skills)

# Step 4: Remove items
skills.remove("Database")
skills.discard("HTML")  # Safe discard
print()
print("After removing items:", skills)

# Step 5: Set operations with another set
advanced_skills = {"AI", "DevOps", "Machine Learning"}
print()
print("Union:", skills.union(advanced_skills))
print("Intersection:", skills.intersection(advanced_skills))
print("Difference:", skills.difference(advanced_skills))
print("Symmetric Difference:", skills.symmetric_difference(advanced_skills))

'''
Sample Output:
Initial set (duplicates removed): {'Python', 'Database', 'Networking'}

Iterating skills:
- Python
- Database
- Networking

After adding items: {'Cloud', 'Security', 'Python', 'Networking', 'AI', 'Database'}

After removing items: {'Cloud', 'Security', 'Python', 'Networking', 'AI'}

Union: {'Cloud', 'Security', 'Python', 'Machine Learning', 'Networking', 'DevOps', 'AI'}
Intersection: {'AI'}
Difference: {'Cloud', 'Security', 'Python', 'Networking'}
Symmetric Difference: {'Cloud', 'Security', 'Python', 'Machine Learning', 'Networking', 'DevOps'}
'''
