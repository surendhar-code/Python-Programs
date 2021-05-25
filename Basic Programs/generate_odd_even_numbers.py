# Develop a python program to generate odd and even numbers using for statement.
n = int(input("Enter the limit : "))
print("The odd numbers are : ")
for i in range(1,n+1,2):
    print(i,end="\t")
print("\n")
print("The even numbers are : ")
for i in range(2,n+1,2):
    print(i,end="\t")