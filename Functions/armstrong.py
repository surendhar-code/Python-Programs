# Develop a python program to find the given number is armstrong number or not using function

def armstrong(n):
    sum=0
    nod = len(str(n))
    while n>0:
        rem = n%10
        sum+=(rem**nod)
        n=n//10

    return sum

n = int(input("Enter the number : "))
if n==armstrong(n):
    print(n," is a armstrong number")
else:
    print(n," is not a armstrong number")
