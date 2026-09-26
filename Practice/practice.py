import math

def calc_triangle():
    b = float(input("Base: "))
    h = float(input("Height: "))
    s1 = float(input("Side 1: "))
    s2 = float(input("Side 2: "))
    s3 = float(input("Side 3: "))
    print(f"Area = {(b * h) / 2}")
    print(f"Perimeter = {s1 + s2 + s3}\n")

def calc_parallelogram():
    b = float(input("Base: "))
    h = float(input("Height: "))
    side = float(input("Adjacent Side: "))
    print(f"Area = {b * h}")
    print(f"Perimeter = {2 * (b + side)}\n")

def calc_rhombus():
    b = float(input("Base side: "))
    h = float(input("Height: "))
    print(f"Area = {b * h}")
    print(f"Perimeter = {4 * b}\n")

def calc_rectangle():
    l = float(input("Length: "))
    w = float(input("Width: "))
    print(f"Area = {l * w}")
    print(f"Perimeter = {2 * (l + w)}\n")

def calc_square():
    l = float(input("Side length: "))
    print(f"Area = {l ** 2}")
    print(f"Perimeter = {4 * l}\n")

def calc_trapezoid():
    b1 = float(input("Top Base (B): "))
    b2 = float(input("Bottom Base (b): "))
    h = float(input("Height: "))
    s1 = float(input("Left Side: "))
    s2 = float(input("Right Side: "))
    print(f"Area = {((b1 + b2) * h) / 2}")
    print(f"Perimeter = {b1 + b2 + s1 + s2}\n")

def calc_circle():
    r = float(input("Radius: "))
    print(f"Area = {math.pi * (r ** 2):.2f}")
    print(f"Circumference = {2 * math.pi * r:.2f}\n")
    
while True:
    print("GEOMETRY CALCULATOR")
    print("1. Triangle")
    print("2. Parallelogram")
    print("3. Rhombus")
    print("4. Rectangle")
    print("5. Square")
    print("6. Trapezoid")
    print("7. Circle")
    print("0. Exit")
    
    choice = input("Choose a shape (0-7): ")
    print()

    if choice == "1":
        calc_triangle()
    elif choice == "2":
        calc_parallelogram()
    elif choice == "3":
        calc_rhombus()
    elif choice == "4":
        calc_rectangle()
    elif choice == "5":
        calc_square()
    elif choice == "6":
        calc_trapezoid()
    elif choice == "7":
        calc_circle()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.\n")