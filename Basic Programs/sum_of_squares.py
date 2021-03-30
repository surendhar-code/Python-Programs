n=int(input("Enter the n value : "))
sum=0
for i in range(1,n+1):
    sum+=i*i
print("Sum of squares of first {0} natural numbers is : {1}".format(n,sum))
