# method 1 - using update() function
def Merge(dict1,dict2):
    return dict1.update(dict2)


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(Merge(dict1, dict2))
print(dict1)

# method 2 - using ** method
def merge2(dict1,dict2):
    temp = {**dict1,**dict2}
    return temp
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(merge2(dict1,dict2))

