import matplotlib.pyplot as plt #pip install numpy
import numpy as np
from scipy.optimize import linprog

c = [-300, -500] # Coeficientes de la función objetivo
A = [[2, 1], [1, 2]] # Coeficientes de las restricciones
b = [230, 250] # Límites de las restricciones
x0_bounds = (0, None) # Límites de x1
x1_bounds = (0, 120) # Límites de x2

res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')


# Calcular los vértices del polígono de la zona factible
vertices = []
for i in range(len(A)):
    res = linprog(c, A_ub=A[:i]+A[i+1:], b_ub=b[:i]+b[i+1:], bounds=[x0_bounds, x1_bounds], method='highs')
    vertices.append(res.x)

print(vertices)

# Plotear el gráfico
x = np.linspace(0, 115, 100)
y1 = 230 - 2 * x
y2 = 250 - x
y3 = 120 * np.ones_like(x)

plt.plot(x, y1, label='2x + y <= 230')
plt.plot(x, y2, label='x + 2y <= 250')
plt.plot(x, y3, label='y <= 120')
plt.fill([v[0] for v in vertices], [v[1] for v in vertices], 'cyan')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()
