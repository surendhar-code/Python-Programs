# Initializing list of dictionaries
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print("Sorting based on age using lambda function and sorted()")
print(sorted(lis,key=lambda i :i['age']))

print("Sorting based on name and age using lambda fn :")
print(sorted(lis,key=lambda i : (i['age'], i['name'])))

print("Sorting based on age in descending order using lambda fn : ")
print(sorted(lis,key=lambda i : i['age'], reverse=True))

