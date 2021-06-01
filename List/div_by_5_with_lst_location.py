'''
Develop a Python program to store ‘N’ numbers in a list and print the
numbers divisible by five with the list location.
'''
lst = [10,40,2,21,50]
print("The numbers divisible by 5 are : ")
for i in range(len(lst)):
    if lst[i]%5==0:
        print("lst[",i,"] = ",lst[i])

