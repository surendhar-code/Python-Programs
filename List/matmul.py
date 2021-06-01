# Develop a python program to multiply two matrices
row1 = int(input("Enter the first matrix rows : "))
col1 = int(input("Enter the columns of the first matrix : "))
row2 = int(input("Enter the second matrix rows : "))
col2 = int(input("Enter the columns of the second matrix : "))

if col1==row2:
    mat=[]
    mata=[]
    matb=[]
    matc=[]

    #creating structure for matrix 1
    for i in range(col1):
        mat.append(0)
    for i in range(row1):
        mata.append(mat.copy())

    #creating structure for matrix 2 and matrix 3
    mat = []
    for i in range(col2):
        mat.append(0)
    for i in range(row2):
        matb.append(mat.copy())
    for i in range(row1):
        matc.append(mat.copy())

    #Entering the elements of the two matrices
    print("Enter the elements of first matrix : ")
    for i in range(row1):
        for j in range(col1):
            mata[i][j] = int(input())
    print("Enter the elements of second matrix : ")
    for i in range(row2):
        for j in range(col2):
            matb[i][j] = int(input())

    # multiplying two matrices
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                matc[i][j] = matc[i][j] + mata[i][k]*matb[k][j]

    # displaying results
    print("The resultant matrix is : ")
    for i in range(row1):
        for j in range(col2):
            print(matc[i][j],end="\t")
        print()