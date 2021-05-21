# Develop a python program to input the mark and print the grade.

mark = int(input("Enter the mark : "))
if mark>=91:
    print("S Grade")
elif mark>=81:
    print("A Grade")
elif mark>=71:
    print("B Grade")
elif mark>=61:
    print("C Grade")
elif mark>=57 and mark<=60:
    print("D Grade")
elif mark>=50:
    print("E Grade")
else:
    print("No Grade")