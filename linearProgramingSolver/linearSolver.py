import numpy as np  #pip install numpy
from scipy.optimize import linprog #pip install scipy

c = [-300, -500] # Coeficientes de la función objetivo ESTAN NEGATIVOS POR QUE SE ESTA MAXIMIZANDO
A = [[2, 1], [1, 2]] # Coeficientes de las restricciones
b = [230, 250] # Límites de las restricciones
x0_bounds = (0, None) # Límites de x1
x1_bounds = (0, 120) # Límites de x2

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
print(res)
print('la solucion (x,y) es: ')
print(res.x)
print('se espera como valor optimo:')
print(abs(res.fun))
