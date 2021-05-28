# Develop a python program to find the sum of N natural numbers using function

def sum_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=i

    return sum

n = int(input("Enter the n value : "))

print("The sum of first {0} natural numbers is : {1} ".format(n,sum_n(n)))
