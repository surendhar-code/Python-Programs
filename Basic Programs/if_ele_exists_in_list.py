lst=[5,6,7,8,2,3,1]
search=int(input("Enter the element to be searched in the list : "))
#using loop and flag method - Method 1
flag=0
for i in range(0,len(lst)):
    if lst[i]==search:
        flag+=1
        break
if flag==0:
    print("The element {0} is not exist in the list".format(search))
else:
    print("The element {0} is exist in the list".format(search))

#using in statement
if search in lst:
    print("The element {0} is  exist in the list".format(search))
else:
    print("The element {0} is not exist in the list".format(search))

