# Develop a pyhton program to count the number of words in a text file
with open('input.txt','r') as f1:
    now =0
    for line in f1:
        words = line.split()
        now+=len(words)

    print("No of words : ",now)
