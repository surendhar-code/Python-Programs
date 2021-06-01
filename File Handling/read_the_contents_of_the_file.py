# Develop a python program to read the contents of a file
with open('input.txt','r') as f:
    filecontents = f.read()
    print(filecontents)