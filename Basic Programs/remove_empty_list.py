#Method 1 - using list comprehension

test_list=[5,6,[],3,[],[],9]
print("The original list is : ",test_list)
lst2=[ele for ele in test_list if ele!=[]]
print("List after removing empty list : ",lst2)

#Method 2 - using filter method
lst3=list(filter(None,test_list))
print("List after removing empty list using filter method : ",lst3)