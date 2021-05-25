# Develop a python program to find the avearge of first n natural numbers without using the formula using for statement.

n = int(input("Enter the limit value : "))
s=0
for i in range(1,n+1):
    s=s+i
print("The average of first n natural numbers : ",s/n)