'''
Develop a Python program to calculate the number of upper case letters
and lower case letters in a string.
'''
def upper_lower(string):
    lower =0
    upper=0
    for i in string:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1

    print("Uppercase count : ",upper)
    print("Lowercase count : ",lower)

s =input("Enter the string : ")
upper_lower(s)













