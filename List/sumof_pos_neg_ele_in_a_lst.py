# Develop a python to find the sum of positive elements and negative elements in a list
lst = [10,20,-10,-4,-5,35,45,-67,-98]
psum=0
nsum=0
for i in range(len(lst)):
    if lst[i]>0:
        psum+=lst[i]
    else:
        nsum+=lst[i]

print("The sum of the positive elements in the list is : ",psum)
print("The sum of the negative elements in the list is : ",nsum)
