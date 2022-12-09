'''
3. Решить систему линейных уравнений 3-го порядка методом обратной матрицы с точностью е=0,001.
Уравнения системы:

                                       2*x1-x2+x3=-3                 
                                       3*x1+5*x2-2*x3=1              
                                       x1-4*x2+10*x3=0
'''

import numpy as np
matrix = np.array([[2,-1,1],[3,5,-2],[1,-4,10]]) # матрица коэффицентов
vecB = np.array([-3,1,0]) # числа, находящиеся справа от знака равно
reverse_matrix = np.linalg.inv(matrix) # обратная матрица к матрице коэффицентов
print(reverse_matrix)
print(vecB)
vecSolve =  reverse_matrix @ vecB # вектор решений с супер-пупер точностью
roundedSolve = np.round(vecSolve,3)
print('Точное решение : ', vecSolve) 
print('Решение e = 0.001: ',roundedSolve)