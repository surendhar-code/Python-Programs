'''
Develop a Python program to read in a list of ‘N’ integers and print its
elements in reverse order without using reverse slicing, reverse method.
'''
lst = [10,20,30,40,50]
print("The reverse of the list are : ")
for i in range(len(lst)-1,-1,-1):
    print(lst[i])

