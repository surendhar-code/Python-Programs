#swap using temporary variable - Method 1
lst_1=[]
n=int(input("Enter the no. of list elements : "))
for i in range(0,n):
    ele=int(input())
    lst_1.append(ele)
print("List before swap : ",lst_1)
pos_1=int(input("Enter the position of frst number : "))
pos_2=int(input("Enter the position of second number : "))
#swap condition
temp=lst_1[pos_1-1]
lst_1[pos_1-1]=lst_1[pos_2-1]
lst_1[pos_2-1]=temp
print("List after swaping two number in a list : ",lst_1)

#using list indexing - Method 2
lst_1=[]
n=int(input("Enter the no. of list elements : "))
for i in range(0,n):
    ele=int(input())
    lst_1.append(ele)
print("List before swap : ",lst_1)
pos_1=int(input("Enter the position of frst number : "))
pos_2=int(input("Enter the position of second number : "))
#condition
lst_1[pos_1-1],lst_1[pos_2-1]=lst_1[pos_2-1],lst_1[pos_1-1]
print("list after swap using indexing method : ",lst_1)

#using tuple variable - Method 3
lst_1=[]
n=int(input("Enter the no. of list elements : "))
for i in range(0,n):
    ele=int(input())
    lst_1.append(ele)
print("List before swap : ",lst_1)
pos_1=int(input("Enter the position of frst number : "))
pos_2=int(input("Enter the position of second number : "))
#condition
get=lst_1[pos_1-1],lst_1[pos_2-1]
lst_1[pos_2-1],lst_1[pos_1-1]=get
print("List after swap using get method : ",lst_1)
