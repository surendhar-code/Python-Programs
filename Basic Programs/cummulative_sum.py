def cummulative(lst):
    cumm_list=[]
    ele=0
    for i in range(len(lst)):
        ele+=lst[i]
        cumm_list.append(ele)
    return cumm_list


lst=[10,20,30,40,50]
print("original list : ",lst)
print("Cummulative sum of the list : ",cummulative(lst))