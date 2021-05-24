# Develop a python program to find the  biggest of 3 numbers using nested if...else statement

a,b,c = [int(x) for x in input("Enter the numbers a, b, c : ").split(',')]
if a>b:
    if a>c:
        print("a is largest number")
    else:
        print("c is largest number")
else:
    if b>c:
        print("b is largest number")
    else:
        print("c is largest number")
