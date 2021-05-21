animals = set(("frog","cat","dog","cow"))
print(animals)
num = {1,2,3,4,5,5,5,5}
print(num)

animals.update(num)
print(animals)

set1 = set(("apple","mango","grapes"))
set2 = set(("apple","microsoft","IBM"))

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)

set1.intersection_update(set2)
print(set1)

set5=set1.symmetric_difference(set2)
print(set5)