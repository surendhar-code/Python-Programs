# Develop a python program to remove the duplicate items from a list.
# Method - 1 using another list
lst1 = [2,11,14,6,6,11]
lst2 = []
for i in lst1:
    if i not in lst2:
        lst2.append(i)
print("The non duplicate elements are : ")
for i in lst2:
    print(i,end="\t")

# Method - 2 using Set
lst1 = [2,11,14,6,6,11]
print("\nThe non duplicate elements are : ")
for i in set(lst1):
    print(i,end="\t")


