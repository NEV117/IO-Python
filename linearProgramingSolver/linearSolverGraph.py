import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Función objetivo
c = [-300, -500] # Coeficientes de la función objetivo

# Restricciones
A = [[2, 1], [1, 2], [1, 1]] # Coeficientes de las restricciones
b = [230, 250, 120] # Límites de las restricciones

# Límites de las variables
x0_bounds = (0, None) # Límite de la primera variable
x1_bounds = (0, None) # Límite de la segunda variable

# Resolución del problema
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Resultados
print("Success: ", res.success)
print("Status: ", res.status)
print("Optimal solution: ", res.fun)
print("Variables: ", res.x)

# Gráfica
plt.plot([0, res.x[0]], [0, res.x[1]], 'ro')
plt.xlabel('UNIF1')
plt.ylabel('UNIF2')
plt.title('Gráfica de la solución óptima')
plt.show()
