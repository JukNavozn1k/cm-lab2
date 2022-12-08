'''
    1. Решить систему линейных уравнений 4-го порядка методом Гаусса с точностью е=0,001.
Уравнения системы:

                                        1,35*x1-1,72*x2-0,62*x3+0,48*x4=0,93             
                                        1,08*x1+0,64*x2-0,95*x3+1,54*x4=1,64             
                                        0,88*x1-0,72*x2+1,36*x3-0,68*x4=-0,85            
                                        0,64*x1+1,48*x2+0,82*x3-1,58*x4=-1,32

'''
import numpy as np
def gaussFunc(matrix):
    # функция меняет матрицу через побочные эффекты
    # если вам нужно сохранить прежнюю матрицу, скопируйте её np.copy
    for nrow, row in enumerate(matrix):
        # nrow равен номеру строки
        # row содержит саму строку матрицы
        divider = row[nrow] # диагональный элемент
        # делим на диагональный элемент.
        row /= divider
        # теперь надо вычесть приведённую строку из всех нижележащих строчек
        for lower_row in matrix[nrow+1:]:
            factor = lower_row[nrow] # элемент строки в колонке nrow
            lower_row -= factor*row # вычитаем, чтобы получить ноль в колонке nrow
    # все строки матрицы изменились, в принципе, можно и не возвращать
    return matrix
def make_identity(matrix):
    # перебор строк в обратном порядке 
    for nrow in range(len(matrix)-1,0,-1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor*row
    return matrix
matrix = np.array([[1.35,-1.72,-0.62,0.48,0.93],
                    [1.08,0.64,-0.95,1.54,1.64],
                    [0.88,-0.72,1.36,-0.68,-0.85],
                    [0.64,1.48,0.82,-1.58,-1.32]])
print(gaussFunc(matrix))
print('############################')
print(make_identity(gaussFunc(matrix)))