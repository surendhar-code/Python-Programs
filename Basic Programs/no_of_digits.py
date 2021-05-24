# Develop a python program to count the number of digits in an integer using while statement
num = int(input("Enter the number : "))
count = 0
while num>0:
    count+=1
    num = num//10
print("The no. of digits in an integer : ",count)
