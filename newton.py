'''
4. Решить систему нелинейных уравнений 2-го порядка методом Ньютона с точностью е=0,001.
Уравнения системы:

                                       6*x+tg(x)*y=0                 
                                       (y^2-2)^2+ln(x)=0

'''
import numpy as np
from math import tan,cos,log
from tabulate import tabulate
def f1(x,y):
    return 6*x + tan(x) *y
def d1fx(x,y):
    return 6 + y*(cos(x)**2)
def d1fy(x,y):
    return tan(x)
def f2(x,y):
    return (y**2-2)**2+log(x)
def d2fx(x,y):
    return 1/x
def d2fy(x,y):
    return 4*y*(y**2 - 2)


def jacobian(x,y):
    return np.array([[d1fx(x,y),d1fy(x,y)],[d2fx(x,y),d2fy(x,y)]])
X = np.array([1E-3,1E-3])
eps = 1E-4
col_names = ['Iteration','x','y','dxSQR','dySQR']
data = []
for i in range(100):    
    x,y = X
    
    
    J = jacobian(x,y)
    delta = np.linalg.solve(J,X)
    NX = X + delta
    dxs,dys = delta[0]**2,delta[1]**2
    if (max(dxs,dys) < eps).all(): break
    X = NX
    
    data.append([i+1,x,y,dxs,dys])
    


print(tabulate(data, headers=col_names, tablefmt="fancy_grid", stralign='center')) 
   
