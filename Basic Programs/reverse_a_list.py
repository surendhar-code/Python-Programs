# python program to reverse a list
# Method -1 reverse method
lst=[10,20,30,40,50,60]
lst.reverse()
print("The list after reversing using reverse attribute : ",lst)
# Method - 2 reversed function
lst=[10,20,30,40,50,60]
rev_list=[ele for ele in reversed(lst)]
print("The list after reversing using reverse attribute : ",rev_list)
# Method -3 slicing techniques
lst=[10,20,30,40,50,60]
print("The list after reversing using reverse attribute : ",lst[::-1])
