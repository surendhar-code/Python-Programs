# Develop a python programs to display only the positive elements of the list

n = int(input("Enter the limit : "))
lst = []
for i in range(0,n):
    a = int(input("Enter the element : "))
    lst.append(a)
print("The positive elements from the list are : ")
for j in range(n):
    if lst[j]>0:
        print(lst[j])
