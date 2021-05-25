# Develop a python program to find that given number is armstrong number or not

num = int(input("Enter the number : "))
pow = len(str(num))
sum=0
temp = num
while num>0:
    rem = num%10
    sum+=(rem**pow)
    num=num//10

if sum == temp:
    print("It is a ARMSTRONG NUMBER")
else:
    print("It is not a ARMSTRONG NUMBER")