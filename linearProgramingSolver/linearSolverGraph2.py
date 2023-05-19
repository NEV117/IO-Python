import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coeficientes de la función objetivo
c = [-300, -500] 

# Restricciones (inecuaciones)
A = [[3, 4], [2, 5], [1, 1]]
b = [450, 600, 150]

# Límites de las variables
x0_bounds = (0, None)
x1_bounds = (0, None)

# Resolviendo el problema de programación lineal
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds],
             method='simplex')

# Imprimiendo la solución
print("Valor máximo de la función objetivo: ", -res.fun)
print("Valores óptimos de las variables: ", res.x)

# Graficando el área factible y la función objetivo
x = np.linspace(0, res.x[0]*1.1, 100)
y = np.linspace(0, res.x[1]*1.1, 100)
X, Y = np.meshgrid(x, y)
Z = c[0]*X + c[1]*Y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis')

for i in range(len(b)):
    ax.plot_surface(X, Y, X*A[i][0]+Y*A[i][1]-b[i], alpha=0.5, color='r')

ax.set_xlabel('X0')
ax.set_ylabel('X1')
ax.set_zlabel('Función objetivo')
plt.show()
