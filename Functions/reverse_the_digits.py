# Develop a python to reverse the digits of the given number using function

def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rem+(rev*10)
        n=n//10

    return rev

n = int(input("Enter the number : "))
print("The reverse of the number is : ",reverse(n))