# Task Sheet No. 10.2: Develop Python for Loops Using range()
# Description: Practice single, double, and triple argument forms of range().

print("Range 1 (stop=5):")
for number in range(5):
    print(number, end=" ")
print()

print()
print("Range 2 (start=1, stop=6):")
for number in range(1, 6):
    print(number, end=" ")
print()

print()
print("Even Numbers (start=2, stop=11, step=2):")
for number in range(2, 11, 2):
    print(number, end=" ")
print()

print()
print("Countdown (start=5, stop=0, step=-1):")
for number in range(5, 0, -1):
    print(number, end=" ")
print()

'''
Sample Output:
Range 1 (stop=5):
0 1 2 3 4 

Range 2 (start=1, stop=6):
1 2 3 4 5 

Even Numbers (start=2, stop=11, step=2):
2 4 6 8 10 

Countdown (start=5, stop=0, step=-1):
5 4 3 2 1 
'''
