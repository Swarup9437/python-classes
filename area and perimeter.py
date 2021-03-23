import math
pi = math.pi
def area_square(a):
    return a**2
def perimeter_square(a):
    return 4*a
def area_rectangle(a,b):
    return a*b
def perimeter_rectangle(a,b):
    return 2*(a+b)
def area_circle(a):
    return pi*(a**2)
def perimeter_circle(a):
    return 2*pi*a

print("Geometry available: ")
print("1. Square")
print("2. Rectangle")
print("3. Circle")
choice1 = input("Select your geometry(1 or 2 or 3): ")
if choice1 == "1":
    num1 = float(input("enter the side of your square(in meter): "))
    print("What you want to calculate? ")
    print("1. Area")
    print("2. Perimeter")
    choice2 = input("select from the above(1 or 2): ")
    if choice2 == "1":
        print(area_square(num1), "Sq. meter is the area of your square.")
    if choice2 == "2":
        print(perimeter_square(num1), "meter is the perimeter of your square.")

if choice1 == "2":
    num1 = float(input("enter the length of your rectangle(in meter): "))
    num2 = float(input("enter the width of your rectangle(in meter): "))
    print("What you want to calculate? ")
    print("1. Area")
    print("2. Perimeter")
    choice2 = input("select from the above(1 or 2): ")
    if choice2 == "1":
        print(area_rectangle(num1,num2), "Sq. meter is the area of your rectangle.")
    if choice2 == "2":
        print(perimeter_rectangle(num1,num2), "meter is the perimeter of your rectangle.")

if choice1 == "3":
    num1 = float(input("enter the radius of your circle(in meter): "))
    print("What you want to calculate? ")
    print("1. Area")
    print("2. Perimeter")
    choice2 = input("select from the above(1 or 2): ")
    if choice2 == "1":
        print(area_circle(num1), "Sq. meter is the area of your circle.")
    if choice2 == "2":
        print(perimeter_circle(num1), "meter is the perimeter of your circle.")



