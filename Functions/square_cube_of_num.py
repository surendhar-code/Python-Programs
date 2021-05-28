# Develop a python program to find the square and cube of a number using a function declaration using the return statement.

def square_cube(n):
    square = n**2
    cube = n**3
    return square,cube

n = int(input("Enter the number : "))
square,cube = square_cube(n)
print("The square of the number {0} is {1}".format(n,square))
print("The cube of the number {0} is {1}".format(n,cube))
