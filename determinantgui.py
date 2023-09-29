from tkinter import *

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

def calculate():
    global matrix1
    matrix1 = [] 
    for i in range(0, dimension):
        matrix1.append([])
        for j in range(0, dimension):
            matrix1[i].append(int(temp_matrix[i][j].get()))
    print(determinant_calculator(matrix1))
    result = determinant_calculator(matrix1)
    resultLabel.config(text=f"Determinant: {result}",bg="#00aaaa")

dimension = int(input("enter the dimension of the matrix: "))
window = Tk()
window.title("Determinant Calculator")
temp_matrix = []
for i in range(0,dimension+1):
    for j in range(0,dimension+1):
        a = max(i,j) - 1
        label = Label(window,text=f"{a}",width=4,height=2,font=("arial",12))
        label.grid(row=i,column=j)
        if i>0 and j!=0:
            break
for i in range(0,dimension):
    temp_matrix.append([])
    for j in range(0,dimension):
        if j == dimension-1:
            paddingx=(4,12)
        else:
            paddingx=4
        entry = Entry(window,width=2,font=("arial",36),bg="#f7ffde")
        entry.grid(row=i+1,column=j+1,padx=paddingx,pady=4)     
        temp_matrix[i].append(entry)

resultLabel = Label(window,text="",font=("arial",18))
resultLabel.grid(row=dimension+2,column=0,columnspan=dimension+1)
calculate_button = Button(window,text="Calculate",command=calculate).grid(row=dimension+1,column=0,columnspan=dimension+1)
window.mainloop()