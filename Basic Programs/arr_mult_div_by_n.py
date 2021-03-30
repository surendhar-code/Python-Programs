#input for array
arr=[]
n=int(input("Enter the size of array : "))
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
#input for number
num=int(input("Enter the divide number : "))

# array multiplication divided by number
mul=1
for i in range(0,n):
    mul = (mul *(arr[i]%num))%num
print("Result is : ",mul)

