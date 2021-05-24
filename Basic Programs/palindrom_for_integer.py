# Develop a python program to check whether the number and its reverse are same or not using while statement
num = int(input("Enter the number : "))
temp = num
rev = 0
while num>0:
    rem = num%10
    rev = rem + (rev*10)
    num=num//10

if temp == rev:
    print("The number and its reverse are same ")
else:
    print("The number and its reverse are not same")