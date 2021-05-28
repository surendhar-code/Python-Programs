# Develop a python program to calculate the length of the string without built in function.

def str_len(string):
    count=0
    for i in string:
        count+=1

    return count

s = input("Enter the string : ")
print("The length of the string is : ",str_len(s))

