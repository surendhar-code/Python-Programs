# Develop a python program to find the sum of the square of individual digits of a number using function

def sum_of_square(n):
    sum=0
    while n>0:
        rem=n%10
        sum=sum+(rem**2)
        n=n//10

    return sum


n = int(input("Enter the number : "))
print("The sum of the square of the individual digits is : ",sum_of_square(n))