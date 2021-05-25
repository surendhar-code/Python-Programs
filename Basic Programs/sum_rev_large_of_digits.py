#  Develop a python program to find the sum of the digits, reversal of the digits and largest of digit using while statement.

num = int(input("Enter the number : "))
s=0
rev=0
large = 0
while num>0:
    rem = num%10
    s=s+rem
    rev = rem +(rev*10)
    if rem>large:
        large = rem

    num = num//10

print("Sum of digits is : ",s)
print("Reverse of the digits is : ",rev)
print("Largest of the digits is : ",large)