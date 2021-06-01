# Develop a python program to display only the negative elements of the list

lst = [10,-2,-3,40,-5]
print("The negative elements are : ")
for i in range(len(lst)):
    if lst[i]<0:
        print(lst[i])