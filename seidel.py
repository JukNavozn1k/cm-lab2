'''
2. Решить систему линейных уравнений 4-го порядка с точностью е=0,0001:
 - методом Зейделя.
Уравнения системы:

                                       x1=0,15*x1+0,05*x2-0,08*x3+0,14*x4-0,48           
                                       x2=0,32*x1-0,43*x2-0,12*x3+0,11*x4+1,24           
                                       x3=0,17*x1+0,06*x2-0,08*x3+0,12*x4+1,15           
                                       x4=0,21*x1-0,16*x2+0,36*x3-0,88
'''

import numpy as np
from numpy import array
from tabulate import tabulate
A = array([[-0.85,0.05,-0.08,0.14],
           [0.32,-1.43,-0.12,0.11],
           [0.17,0.06,-1.08,0.12],
           [0.21,-0.16,0.36,-1]])
 
b = array([[0.48],[-1.24],[-1.15],[0.88]])
m = len(A)
x = [.0 for i in range(m)]
Iteration = 0
converge = False
pogr = 0.
col_names = ['Iteration','x1','x2','x3','x4','d']
data = []

while not converge:
    x_new = np.copy(x)
    for i in range(m):
        s1 = sum(A[i][j] * x_new[j] for j in range(i))
        s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
        x_new[i] = (b[i] - s1 - s2) / A[i][i]
    pogr = sum(abs(x_new[i] - x[i])  for i in range(m))
    converge =  pogr < 1e-4 # <=========================  epsilon
    Iteration += 1
    x = x_new
    data.append([Iteration,x[0],x[1],x[2],x[3],pogr])

print(tabulate(data, headers=col_names, tablefmt="fancy_grid", stralign='center')) 