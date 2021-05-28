"""Develop a Python program using functions that will compute and print the
area of any four geometric shapes. Write a main function to get the input
and invoke the function using conditional statement. """

def circle(r):
    return 3.14*r*r

def square(a):
    return a**2

def rectangle(l,b):
    return l*b

def triangle(b,h):
    return 0.5*b*h


print("1.Circle | 2. Square | 3.Rectangle | 4.Triangle")
choice = int(input("Enter the choice : "))
if choice == 1:
    rad = float(input("Enter the radius value : "))
    print("Area of the circle is : ",circle(rad))

elif choice == 2:
    a = float(input("Enter the side of the square : "))
    print("Area of the square is : ",square(a))

elif choice == 3:
    l,b = [int(x) for x in input("Enter the length and breadth of the rectangle : ").split()]
    print("Area of the rectangle is : ",rectangle(l,b))

elif choice==4:
    b,h = [int(x) for x in input("Enter the base and height of the triangle : ").split()]
    print("Area of the triangle : ",triangle(b,h))

else:
    print("Invalid Choice... Choos the right choice")