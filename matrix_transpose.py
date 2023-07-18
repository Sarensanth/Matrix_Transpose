def matrix_transpose(matrix,rows,columns):

    column=len(matrix[0])
    transpose = [[0 for i in range(rows)] for j in range(column)]

    for i in range(rows):
        for j in range(column):
            transpose[j][i] = matrix[i][j]

    return transpose

matrix=[]
rows=int(input("Enter number of rows : "))
columns=int(input("Enter number of columns : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))

print(matrix_transpose(matrix,rows,columns))