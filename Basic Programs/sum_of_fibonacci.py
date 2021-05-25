# Develop a python program to find the sum of fibonacci series using for loop
n = int(input("Enter the terms : "))
a=-1
b=1
sum = 0
for i in range(1,n+1):
    c=a+b
    sum+=c
    a=b
    b=c

print("The sum of fibonacci series of n terms is : ",sum)
