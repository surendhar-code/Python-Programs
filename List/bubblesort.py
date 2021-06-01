# Develop a python program to sort a list of N numbers using bubble sort.
lst = [5,1,9,3,2]
for i in range(len(lst)):
    for j in range(0,len(lst)-i-1):
        if lst[j]>lst[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp

print("The elements after sorting are : ")
print(lst)