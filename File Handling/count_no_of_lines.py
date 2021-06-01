# Develop a Python program to count the number of lines in a text file.
with open('input.txt','r') as f:
    nol = 0
    for line in f:
        nol+=1
    print("The no. of lines in a text file : ",nol)