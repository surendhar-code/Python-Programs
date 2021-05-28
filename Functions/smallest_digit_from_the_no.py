# Develop a python program to find the smallest digit from the number

def smallest(n):
    small=9
    while n>0:
        rem=n%10
        if rem<small:
            small=rem
        n=n//10

    return small

n = int(input("Enter the number : "))
print("The smallest number from the number is : ",smallest(n))