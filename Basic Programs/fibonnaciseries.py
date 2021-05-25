# Develop a python program to print the first 'n' terms of the fibonnacci series

n = int(input("Enter the n terms : "))
a=-1
b=1
print("The fibonacci series are : ")
for i in range(1,n+1):
    c=a+b
    print(c,end="\t")
    a=b
    b=c
