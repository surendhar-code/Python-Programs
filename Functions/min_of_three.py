# Develop a python program to find the minimum of given three numbers using parameter passing

def minimum(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c


n1,n2,n3 = [int(x) for x in input("Enter the three numbers : ").split()]
print("The minimum of three numbers is : ",minimum(n1,n2,n3))
