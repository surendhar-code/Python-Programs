x = lambda i : i+10
print(x(2))

y = lambda j : j*2
print(y(2))

z= lambda a,b,c : a+b+c
print(z(2,3,4))

def myfun(n):
    return lambda i : i*n
x = myfun(2)
y = x(3)
print(y)