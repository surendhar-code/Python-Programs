# Develop a python program to subtract two matrices
row  = int(input("Enter the number of rows : "))
col = int(input("Enter the number of cols : "))
mat=[]
mata=[]
matb=[]
matc=[]
for i in range(col):
    mat.append(0)
#creating matrix structure
for i in range(row):
    mata.append(mat.copy())
    matb.append(mat.copy())
    matc.append(mat.copy())
print("Enter the elements of matrix A : ")
for i in range(row):
    for j in range(col):
        mata[i][j] = int(input())
print("Enter the elements of matrix B : ")
for i in range(row):
    for j in range(col):
        matb[i][j] = int(input())

# subtracting two matrices
for i in range(row):
    for j in range(col):
        matc[i][j] = mata[i][j] - matb[i][j]
print("The resultant matrix is : ")
for i in range(row):
    for j in range(col):
        print(matc[i][j],end='\t')
    print()