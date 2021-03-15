my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky', 'nerdy', 'geek', 'love',
           'questions', 'words', 'life']

def divide_chunks(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]








N=int(input("Enter no.of elements the list should have : "))
x=list(divide_chunks(my_list,N))
print("The chunked list : ",x)