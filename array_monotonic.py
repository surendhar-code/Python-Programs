#function to find monotonic or not
def array_monotonic(arr):
    return (all(arr[i]<=arr[i+1] for i in range(len(arr)-1)) or all(arr[i]>=arr[i+1] for i in range(len(arr)-1)))

#size of array
n=int(input("Enter the size of array : "))

#getting input for array
arr=[]
for i in range(0,n):
    ele=int(input())
    arr.append(ele)

#printing monotonic or not
if(array_monotonic(arr)):
    print("The given array is monotonic")
else:
    print("The given array is not monotonic")

