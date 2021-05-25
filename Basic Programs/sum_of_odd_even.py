# Develop a python program to find the sum of odd and even numbers using for loop
n = int(input("Enter the limit : "))
oddsum = 0
evensum = 0
for i in range(1,n+1):
    if i%2==1:
        oddsum+=i
    else:
        evensum+=i
print("The sum of odd numbers : ",oddsum)
print("The sum of even numbers : ",evensum)