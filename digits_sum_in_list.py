lst=[12,67,98,34]
print("The orignal list is : ",lst)

digits=[]
for ele in lst:
    sum=0
    for digit in str(ele):
        sum+=int(digit)
    digits.append(sum)

print("List digits sum : ",digits)