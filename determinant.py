from fractions import Fraction

def matrix_printer(matrix):    #function to print matrices   
    dimension = len(matrix)
    for i in range(0,dimension):
        print("|",end="")
        for j in range(0,dimension):
            if j == dimension -1:
                print(f"{Fraction(matrix[i][j]).limit_denominator()}", end=" ")
            else:
                print(f"{Fraction(matrix[i][j]).limit_denominator()}", end=" ")     
        print("|",end="")
        print()

def matrix_partitioner(matrix,i,j):    #remove ith row and jth column
    dimension = len(matrix)
    new_matrix = []
    for x in range(0,dimension-1):
        new_matrix.append([])
        for y in range(0,dimension-1):
            new_matrix[x].append(0)
            if x < i and y < j:
                new_matrix[x][y] = matrix[x][y]
            elif x < i and y >= j:
                new_matrix[x][y] = matrix[x][y+1]
            elif x >= i and y < j:
                new_matrix[x][y] = matrix[x+1][y]
            else:
                new_matrix[x][y] = matrix[x+1][y+1]
    return new_matrix

def determinant_calculator(matrix):    #function to calculate determinant
    dimension = len(matrix)
    determinant = 0
    for x in range(0,dimension): 
        if dimension == 1:
            determinant = matrix[0][0]
        elif dimension != 1 and x % 2 == 0:
            determinant +=  determinant_calculator(matrix_partitioner(matrix,x,0)) * matrix[x][0]
        elif dimension != 1 and x % 2 != 0:
            determinant -= determinant_calculator(matrix_partitioner(matrix,x,0)) * matrix[x][0]
    return determinant

rows = int(input("enter the dimension of matrix: "))
columns = rows
matrix = []
for i in range(0,rows):
    matrix.append([])
    for j in range(0,columns):
        print(f"entry in row {i+1}, column {j+1}: ",end = "")
        matrix[i].append(int(input()))

print("---------------------------")
matrix_printer(matrix)
print("determinant: ",end=" ")
print(determinant_calculator(matrix))