# Develop a python program to add two matrices
row   = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns : "))
mat = []
mata = []
matb = []
matc = []
for i in range(col):
    mat.append(0)

for i in range(row):
    mata.append(mat.copy())
    matb.append(mat.copy())
    matc.append(mat.copy())

print("Enter the elements of the matrix A : ")
for i in range(row):
    for j in range(col):
        mata[i][j] = int(input())

print("Enter the elements of the matrix B : ")
for i in range(row):
    for j in range(col):
        matb[i][j] = int(input())

# adding two matrices
for i in range(row):
    for j in range(col):
        matc[i][j] = mata[i][j] + matb[i][j]
print("The resultant matrix is : ")
for i in range(row):
    for j in range(col):
        print(matc[i][j],end="\t")
    print()
