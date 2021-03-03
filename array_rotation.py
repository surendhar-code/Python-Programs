arr=[10,20,30,40,50]
print("Array before rotation : ",arr)
by=int(input("Enter the array rotation by value : "))
n=len(arr)
#storing into the temp array
temp=[]
for i in range(0,by):
    temp.append(arr[i])
#shifting the normal array
for i in range(by,n):
    arr[i-by]=arr[i]
#appending temp array to normal array
for i in range(0,by):
    arr[n-(by-i)]=temp[i]


print("Array after rotation : ",arr)