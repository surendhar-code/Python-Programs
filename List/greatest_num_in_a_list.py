'''
Develop a Python program to find the greatest of ’N’ numbers stored in a
list and print the result.
'''
# Method  - 1 using max() function
lst = [10,20,30,40,50]
print("The greatest element in a list is ",max(lst))

# Method 2 using temp variable
lst = [10,20,30,40,50]
large =0
for i in lst:
    if i>large:
        large=i
print("The greatest element in a list is ",large)
