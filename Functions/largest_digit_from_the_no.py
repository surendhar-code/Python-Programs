# Develop a python program to find the largest digit from the number using functions

def largest(n):
    large=0
    while n>0:
        rem=n%10
        if rem>large:
            large=rem
        n=n//10

    return large

n = int(input("Enter the number : "))
print("The largest digit from the number is : ",largest(n))