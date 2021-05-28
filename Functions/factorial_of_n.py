# DEvelop a python program using function to compute the factorial of a given number.
def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n=n-1

    return fact

n = int(input("Enter the number : "))
print("The factorial is : ",factorial(n))