# Develop a python program to find the factorial of a given number using while statement.
n=int(input("Enter the number : "))
temp = n
fact=1
while n>0:
    fact=fact*n
    n=n-1

print("The factorial of the number ",temp," is : ",fact)