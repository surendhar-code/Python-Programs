# Method - 1 using for loop
lst=[10,20,30,40,50]
multiply=1
for i in lst:
    multiply*=i
print("Multiply of all elements in the list",multiply)

# Method -2 using math.prod()
import math
mul=math.prod(lst)
print("Multiply of all elements in the list using math.prod()",mul)

