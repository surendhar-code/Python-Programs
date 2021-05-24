# Develop a python program to reverse the digits of a given number using while statement
num = int(input("Enter the number : "))
rev = 0
while num>0:
    rem = num%10
    rev = rem + (rev*10)
    num=num//10
print("The reversed number = ",rev)