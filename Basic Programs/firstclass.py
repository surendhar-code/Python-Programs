def add(x):
    return x+20

a = add
print(a(10))

#method 2
def mult(func):
    return func*10

print("Passing function as parameters to another function : ",mult(add(10)))

def string():
    def upper(val):
        return val.upper()

    return upper

x = string()
print("Function returning function : ",x("suren"))

