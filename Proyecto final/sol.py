import numpy as np
from scipy.optimize import linprog

# Coeficientes de la función objetivo
c = [-3, -2, 1, -4]

# Coeficientes de las restricciones
A = [[2, 3, -1, 2],
     [4, -2, 2, 1],
     [-1, -1, -1, -1],
     [1, 1, 2, 1]]

# Lados derechos de las restricciones
b = [10, 8, -5, 6]

# Rangos de las variables
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)
x4_bounds = (0, 1)

# Resolver el problema utilizando el método simplex
result = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds, x3_bounds, x4_bounds], method='simplex')

# Imprimir el estado de la solución
print("Estado:", result.message)

# Imprimir los valores óptimos de las variables de decisión
print("Valores óptimos de las variables:")
print("x1 =", result.x[0])
print("x2 =", result.x[1])
print("x3 =", result.x[2])
print("x4 =", result.x[3])

# Imprimir el valor óptimo de la función objetivo
print("Valor óptimo de Z =", -result.fun)
