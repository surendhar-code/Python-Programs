a=10

def fun1():
    print("value of a Inside fun1 : ",a)

def fun2():
    a=50
    print("value of a inside fun2 : ",a)

def fun3():
    global a
    print("Value of a inside func3 : ",a)
    a=100
    print("value of a inside func3",a)






print("value of a :",a)
fun1()
print("value of a :",a)
fun2()
print("value of a :",a)
fun3()
print("Value of a is: ",a)