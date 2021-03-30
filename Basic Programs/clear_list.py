# Clearing a list using different methods
#Method 1 - using clear() function
lst=[5,6,9,2,1,3,4,7]
print("List before clearing using clear() function : ",lst)
lst.clear()
print("List after clearing using clear() : ",lst)

#Method 2 - using reinitialization empty list
lst=[5,6,9,2,1,3,4,7]
print("List before clearing using reinitialization method : ",lst)
lst2=[]
lst=lst2
print("List after clearing using reinitialization method : ",lst)

#Method 3 - using del method
lst=[5,6,9,2,1,3,4,7]
print("List before clearing using del() : ",lst)
del(lst[:])
print("List after clearing using del() method : ",lst)

#Method 4 - using *=0
lst=[5,6,9,2,1,3,4,7]
print("List before clearing using *=0 : ",lst)
lst *=0
print("List after clearing using *=0 : ",lst)




