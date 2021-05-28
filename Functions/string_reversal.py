# Develop a python program  to accept a word from the user and reverse it without using any string modules

def str_reverse(string):
    return string[::-1]

s = input("Enter the string : ")
print("The reverse of the string is : ",str_reverse(s))

