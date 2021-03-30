n=int(input("Enter the n value : "))
sum=0
for i in range(1,n+1):
    sum+=i*i*i
print("Cube sum of  first {0} natural numbers is : {1}".format(n,sum))
