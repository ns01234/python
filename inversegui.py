from tkinter import *
from fractions import Fraction

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

def inverse_matrix(matrix):    #1/|detA| * adjA
    global inverse
    dimension = len(matrix)
    a = determinant_calculator(matrix)
    if a == 0:
        print("Inverse does not exist.")
        return None
    inverse = []
    for j in range(0,dimension):
        inverse.append([])
        for i in range(0,dimension):
            sign = (-1) ** (i+j)
            inverse[j].append((sign * determinant_calculator(matrix_partitioner(matrix,i,j)) / (determinant_calculator(matrix))))
    return inverse

def determinant():
    global matrix1
    matrix1 = [] 
    for i in range(0, dimension):
        matrix1.append([])
        for j in range(0, dimension):
            matrix1[i].append(int(temp_matrix[i][j].get()))
    result = determinant_calculator(matrix1)
    determinantLabel=Label(window,text="",font=("arial",18))
    determinantLabel.grid(row=dimension+4,column=0,columnspan=dimension+1)
    determinantLabel.config(text=f"Determinant: {result}",bg="#00aaaa")

def inverse():
    global matrix1
    matrix1 = [] 
    for i in range(0, dimension):
        matrix1.append([])
        for j in range(0, dimension):
            matrix1[i].append(int(temp_matrix[i][j].get()))
    inverselabel = Label(window,text="Inverse: ",font=(32))
    inverselabel.grid(row=0,column=dimension+1,rowspan=dimension+3)
    for i in range(0,dimension+1):
        for j in range(dimension+2,2*dimension+3):
            a = max(i,j-dimension-2)
            if i == 0 or j == dimension+2:
                numlabel = Label(window,text=f"{a}",width=4,height=2,font=("arial",12),bg="#d5e8f5")
                numlabel.grid(row=i,column=j)
    for i in range(0,dimension):
        for j in range(0,dimension):
                numlabel = Label(window,text=f"{Fraction((inverse_matrix(matrix1))[i][j]).limit_denominator()}",width=3,height=1,font=("arial",36),bg="#f7ffde")
                numlabel.grid(row=i+1,column=j+dimension+3,padx=4,pady=4)
    
            
dimension = int(input("enter the dimension of the matrix: "))
window = Tk()
window.title("Determinant Calculator")
temp_matrix = []
for i in range(0,dimension+1):
    for j in range(0,dimension+1):
        if i>0 and j!=0:
            break
        a = max(i,j) - 1
        label = Label(window,text=f"{a}",width=4,height=2,font=("arial",12),bg="#d5e8f5")
        label.grid(row=i,column=j)
for i in range(0,dimension):
    temp_matrix.append([])
    for j in range(0,dimension):
        if j == dimension-1:
            paddingx=(4,12)
        else:
            paddingx=4
        entry = Entry(window,width=2,font=("arial",32),bg="#f7ffde")
        entry.grid(row=i+1,column=j+1,padx=paddingx,pady=4)     
        temp_matrix[i].append(entry)
    
determinant_button = Button(window,text="Determinant",command=determinant).grid(row=dimension+2,column=0,columnspan=dimension+1)
inverse_button = Button(window,text="Inverse",command=inverse).grid(row=dimension+3,column=0,columnspan=dimension+1)
window.configure(bg="#d5e8f5")
window.mainloop()
