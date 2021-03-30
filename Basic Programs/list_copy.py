#Method 1 - using copy() method
lst1=[10,20,30,40,50]
lst2=lst1.copy()
print("original list : ",lst1)
print("New copied list : ",lst2)

# Method 2 - using list comprehension
lst3=[ele for ele in lst1]
print("Copied list using list comprehension : ",lst3)