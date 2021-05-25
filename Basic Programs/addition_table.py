# Develop a python program to print addition table of the given number using for statement

t = int(input("Enter the table : "))
n = int(input("Enter the limit"))
for i in range(1,n+1):
    print(i," + ",t," = ",i+t)
