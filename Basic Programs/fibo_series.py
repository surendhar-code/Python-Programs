nterms=int(input("Enter the terms : "))
n1,n2=0,1
count=0
if(nterms<0):
    print("Enter the positive integer")
elif nterms==1:
    print("The fibonacci series upto {0} terms is {1}".format(nterms,n1))
else:
    while count<nterms:
        print(n1)
        #update values
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
