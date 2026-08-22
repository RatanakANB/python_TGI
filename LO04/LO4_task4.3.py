# Task Sheet No. 4.3: Apply Python String Methods and Search Strings
# Description: Use built-in string methods to manipulate string values and search for characters and phrases

# Create string variable
message = "  Python Programming is Easy  "

# Applying String Methods
print(message.upper())
print(message.lower())
print(message.title())
print(message.strip())
print(message.replace("Easy", "Powerful"))
print(message.split())
print(message.find("Python"))

# Searching within string
print("Python" in message)
print("Java" not in message)

'''
Sample Output:
  PYTHON PROGRAMMING IS EASY  
  python programming is easy  
  Python Programming Is Easy  
Python Programming is Easy
  Python Programming is Powerful  
['Python', 'Programming', 'is', 'Easy']
2
True
True
'''
