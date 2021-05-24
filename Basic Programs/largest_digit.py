# Develop a python program to find the largest digit of a number using while statement
num = int(input("Enter the number : "))
large =0
while num>0:
    rem =num%10
    if rem>large:
        large=rem
    num=num//10

print("The largest digit = ",large)