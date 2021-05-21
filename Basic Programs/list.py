lst = ["suren",1,True,2.3]
print(lst)

lst.append('Ramesh')
lst.insert(0,"Suresh")
print(lst)

lst1 = list((10,20,30,40,50))
print(lst1)
print(lst1[-5:0])
print(lst1[::-1])

#lst1[1:2]=[100,200]
#lst1[1:2]=[100,200]
lst1[1:3]=["Dhoni","Dhoni"]
print(lst1)

lst1.extend(lst)
print(lst1)

lst1.remove("Dhoni")
print(lst1)
lst1.pop()
print(lst1) # ramesh got deleted
lst1.pop(4)
print(lst1)
del lst1[0]
print(lst1)
#del lst
#print(lst)
lst2 = list((range(0,10)))
print(lst2)
lst2.clear()
print(lst2) # clears the list

fruits = list(("apple","orange","grapes","pineapple","Guava"))
newlist = [x for x in fruits if x!="apple"]
print(newlist)

fruits = list(("apple","orange","grapes","pineapple","Guava"))
newlist = [x if x!="orange" else "mango" for x in fruits]
print(newlist)

vegetables = ["carrot","Tomato","potato","Onion","brinjal","Capsicum"]
vegetables.sort()
print(vegetables)
vegetables.sort(reverse=True)
print(vegetables)
vegetables.sort(key=str.lower)
print(vegetables)


vegetables = ["onion","carrot"]
veg3 = vegetables
veg=vegetables.copy()
print(veg)
veg2 = list(vegetables)
print(veg2)

vegetables.append("beetroot")
print(veg)
print(veg2)

print("Index : ",vegetables.index("onion"))