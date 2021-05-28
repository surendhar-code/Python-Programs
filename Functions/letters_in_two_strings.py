'''
Develop a Python program to using Generator function to print all the letters from
word1 that also appear in word2.
'''

def str_both(str1,str2):
    for i in str1:
        if i in str2:
            yield i




str1 = input("Enter the string1 : ")
str2 = input("Enter the string2 : ")
letter_in_both = str_both(str1,str2)
for s in letter_in_both:
    print(s)











