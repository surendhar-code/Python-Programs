# Develop a python program to find the sum of digits of a number

def sumofdigits(n):
    sum=0
    while n>0:
        rem=n%10
        sum=sum+rem
        n=n//10

    return sum


n = int(input("Enter the number : "))
print("The sum of the digits of the number is : ",sumofdigits(n))