start_interval=int(input("Enter the start interval : "))
stop_interval=int(input("Enter the stop interval : "))
for i in range(start_interval,stop_interval+1):
    if i>1:
        for j in range(2, start_interval):
            if (i % j == 0):
                break
        else:
            print(i)


