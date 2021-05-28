# Develop a python program using function, to check whether the given number and its reverse are same

def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rem+(rev*10)
        n=n//10

    return rev

n = int(input("Enter the number : "))
if n == reverse(n):
    print("The reverse and original number are same")
else:
    print("The reverse and original number are not same")