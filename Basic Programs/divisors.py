# Develop a python program to print all the divisors for the given number
num = int(input("Enter the number : "))
print("The divisors of number {0} are ".format(num))
for i in range(1,num+1):
    if num%i == 0:
        print(i,end="\t")
