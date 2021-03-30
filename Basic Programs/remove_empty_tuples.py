lst1=[23,12,45,(),6,(),8,()]
lst2=[ele for ele in lst1 if ele!=()]
lst3=list(filter(None,lst1))
print("Original List : ",lst1)
print("List after removing empty tuples using list comprehension : ",lst2)
print("List after removing empty tuples using filter method : ",lst3)