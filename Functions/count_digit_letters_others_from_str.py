'''
Develop a Python program that accepts a string and count the number of
digits, letters and other characters.
'''

def str_count(string):
    digits =0
    letters =0
    others=0
    for i in string:
        if i.isdigit():
            digits+=1
        elif i.isalpha():
            letters+=1
        else:
            others+=1

    return digits,letters,others

s = input("Enter the string : ")
n_digits,n_letters,n_others = str_count(s)
print("Digits : {0} \n Letters : {1} \n Others : {2}".format(n_digits,n_letters,n_others))
