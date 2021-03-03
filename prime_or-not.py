num=int(input("Enter the number : "))
for i in range(2,num):
    if num%i==0:
        print("The no. {0} is not a prime number".format(num))
        break
else:
    print("The no. {0} is  a prime number".format(num))