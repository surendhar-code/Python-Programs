'''
Develop a Python program to read marks of 10 students in the range of 0 -
100. Then make 10 groups: 0-10, 10-20, 20-30, etc. Count the number of
values that falls in each group and display the results.

'''

a = []
for i in range(10):
    print("Enter the mark of the student",i+1," : ")
    a.append(int(input()))
mark = []
for i in range(10):
    mark.append(0)
for i in a:
    if i<=10:
        mark[0]+=1
    elif i<=20:
        mark[1]+=1
    elif i<=30:
        mark[2]+=1
    elif i<=40:
        mark[3]+=1
    elif i<=50:
        mark[4]+=1
    elif i<=60:
        mark[5]+=1
    elif i<=70:
        mark[6]+=1
    elif i<=80:
        mark[7]+=1
    elif i<=90:
        mark[8]+=1
    elif i<=100:
        mark[9]+=1

    print("The result is : ")
    for i in range(10):
        print(i*10+1, "-", i*10+10, ":",mark[i])













