# Develop a python program to print the numbers that are divisible by a given number using for statement
n = int(input("Enter the limit : "))
d = int(input("Enter the number : "))
print("The numbers divisible by {0} are : ".format(d))
for i in range(1,n+1):
    if i%d==0:
        print(i,end="\t")