num=int(input("Enter the number : "))
fact=1
temp=num
while(temp>0):
    fact*=temp
    temp-=1
print("The factorial of the number {0} is {1}".format(num,fact))