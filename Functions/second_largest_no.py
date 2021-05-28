# Develop a python program to find the largest digit from a number using function.

def second_largest(n):
    fl = 0
    sl = 0
    while n>0:
        rem = n%10
        if rem>fl:
            sl=fl
            fl=rem
        elif rem>sl:
            sl=rem

        n=n//10

    return sl

n = int(input("Enter the number : "))
print("The largest number is : ",second_largest(n))
