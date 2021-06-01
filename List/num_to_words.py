# Develop a python program to accept any number and print its in words
n = input("Enter the number : ")
num_lst = list(n)

words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
"Eight", "Nine"]
for i in range(len(num_lst)):
    print(words[int(num_lst[i])],end=" ")