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
 
A = array([[2,-1,1],[3,5,-2],[1,-4,10]])
 
b = array([[-3],[1],[0]])
m = len(A)
x = [.0 for i in range(m)]
Iteration = 0
converge = False
pogr = 0.
while not converge:
    x_new = np.copy(x)
    for i in range(m):
        s1 = sum(A[i][j] * x_new[j] for j in range(i))
        s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
        x_new[i] = (b[i] - s1 - s2) / A[i][i]
    pogr = sum(abs(x_new[i] - x[i])  for i in range(m))
    converge =  pogr < 1e-6 # <=========================  epsilon
    Iteration += 1
    x = x_new
print('Количество итераций :', Iteration)
print('Решение системы уравнений :', x)
print('Погрешность :', pogr)