def duplicate(lst):
    size=len(lst)
    repeated=[]
    for i in range(size):
        k=i+1
        for j in range(k,size):
            if lst[i]==lst[j] and lst[i] not in repeated:
                repeated.append(lst[i])

    return repeated

lst1=[10,56,45,10,56,63,98,63]
print("The duplicate elements in the list are : ",duplicate(lst1))