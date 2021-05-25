# Develop a python program to find the value of x power n using while statement
x = int(input("Enter the x value : "))
n = int(input("Enter the n value : "))
s=1
i=1
while i<=n:
    s*=x
    i=i+1

print("The result is : ",s)