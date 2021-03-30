from operator import itemgetter
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print("The list printed sorting by age : ")
print(sorted(lis,key=itemgetter('age')))

print("The list printed sorting by age and name : ")
print(sorted(lis,key=itemgetter('age','name')))

print("The list printed sorting by age in descending order : ")
print(sorted(lis, key=itemgetter('age'), reverse=True))