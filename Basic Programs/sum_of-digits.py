# Develop a python program to find the sum of digits in an integer using while statement.

num = int(input("Enter the number : "))
sum = 0
while num>0:
    rem = num%10
    sum+=rem
    num=num//10
print("The sum of digits is : ",sum)