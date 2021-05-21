# Develop a python program to find the cutoff marks in an engineering admission using if statement.

cutoff = float(input("Enter cutoff mark : "))
quota  = int(input("Enter the quota 1 - General 2 - Sports : "))
if quota == 2:
    cutoff+=5
print("Cutoff mark = ",cutoff)