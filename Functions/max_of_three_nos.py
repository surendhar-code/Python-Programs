# DEvelop a python program to find maximum of given three numbers using parameter passing.

def max_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


n1,n2,n3 = [int(x) for x in input("Enter the three numbers : ").split()]
print("The largest of the three numbers is : ",max_three(n1,n2,n3))