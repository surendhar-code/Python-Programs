# Develop a python program to find whether the given number is perfect number or not
n = int(input("Enter the number : "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i

if n==sum:
    print("It is a perfect number")
else:
    print("It is not a perfect number")