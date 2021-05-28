# Develop a python program to count the no. of vowels in the given string

def vowels(string):
    vow = 0
    for i in string:
        if i in "aeiouAEIOU":
            vow+=1
    return vow

s = input("Enter the string : ")
print("The count of the vowels in the string {0} is {1}".format(s,vowels(s)))