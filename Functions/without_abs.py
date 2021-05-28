# Develop a python program to find the absolute value of the number without using abs function

def abs(n):
    if n<0:
        return -n
    else:
        return n

n = int(input("Enter the number : "))
print("The absolute value of the number : ",abs(n))