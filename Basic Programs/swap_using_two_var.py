num1,num2 = [int(x) for x in input("Enter the values : ").split()]
print("Before Swapping : ")
print("num1 : {0} num2 : {1}".format(num1,num2))
num1 = num1+num2
num2 = num1 - num2
num1 = num1 - num2
print("After Swapping : ")
print("num1 : {0} num2 : {1}".format(num1,num2))