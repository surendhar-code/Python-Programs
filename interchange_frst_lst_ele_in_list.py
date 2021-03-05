#getting input from the user
lst_1=[]
n=int(input("Enter the no. of list elements : "))
for i in range(0,n):
    ele=int(input())
    lst_1.append(ele)
print("List before interchanging : ",lst_1)
#interchanging using swap condition
temp=lst_1[0]
lst_1[0]=lst_1[n-1]
lst_1[n-1]=temp
print("List after interchanging : ",lst_1)

#using list indexing
lst_2=[]
n=int(input("Enter the no. of list elements : "))
for i in range(0,n):
    ele=int(input())
    lst_2.append(ele)
print("List before interchanging : ",lst_2)
lst_2[0],lst_2[-1]=lst_2[-1],lst_2[0]
print("List interchanging using list indexing : ",lst_2)

#using tuple variable get
lst_3=[]
n=int(input("Enter the no. of list elements : "))
for i in range(0,n):
    ele=int(input())
    lst_3.append(ele)
print("List before interchanging : ",lst_3)
get = lst_3[-1],lst_3[0]
lst_3[0],lst_3[-1]=get
print("List interchanging tuple variable get ",lst_3)
