num=int(input("Enter the input number : "))
#calculate the length of the number
len_num=len(str(num))
#calculate armstrong no
temp=int(num)
armstrong=0

while(temp>0):
    rem=temp%10
    armstrong+=rem**len_num
    temp//=10

#Checking armstrong no. or not
if(armstrong==num):
    print("The number {0} is armsrong number".format(num))
else:
    print("The number {0} is not a armstrong number".format(num))