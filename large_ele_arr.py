#using built-in function
arr=[10,56,85,32,22]
print("The largest element in array is : ",max(arr))

# using loop method
def largest_in_array(arr,n):
    large=arr[0]
    for i in range(1,n):
        if arr[i]>large:
            large=arr[i]
    return large

print("The largest element in the array using function is : ",largest_in_array(arr,len(arr)))
