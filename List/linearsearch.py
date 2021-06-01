# Develop a python program to search an element from a list of N numbers using linear search

def linearsearch(lst,ele):
    for i in range(len(lst)):
        if lst[i] == ele:
            return i

    return -1

lst = [10,20,30,40]
ele = int(input("Enter the element to be searched : "))
pos = linearsearch(lst,ele)
if pos == -1:
    print("The element is not available in the list")
else:
    print("The element is found at the location : ",pos)
