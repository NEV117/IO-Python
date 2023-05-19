import matplotlib.pyplot as plt #pip install matplotlib
import numpy as np #pip install numpy
from scipy.optimize import linprog #pip install scipy

# Coeficientes de la función objetivo (se maximiza)
c = [-300, -500]

# Coeficientes de las restricciones
A = [[2, 1], [1, 2]]

# Límites de las restricciones
b = [230, 250]

# Límites de las variables
x0_bounds = (0, None)
x1_bounds = (0, 120)

# Resolución del problema
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')

# Solución
sol = res.x

# Puntos de los vértices del área factible
vertices = [(0, 120), (10, 120), (70, 90), (55,120), (115, 0), (0,0)]
xx = [v[0] for v in vertices]
yy = [v[1] for v in vertices]

# Rangos de las variables x y y
x = np.linspace(0, 115, 100)
y1 = 230 - 2 * x
y2 = 250 - x
y3 = 120 * np.ones_like(x)

# Gráfico de las restricciones y el área factible
plt.plot(x, y1, label='2x + y <= 230')
plt.plot(x, y2, label='x + 2y <= 250')
plt.plot(x, y3, label='y <= 120')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.fill(xx, yy, 'cyan')
plt.axis('equal')

# Punto de la solución
plt.scatter(sol[0], sol[1], color='green', s=50)

# Anotacion de la solucion
plt.annotate(f"x = {int(res.x[0])}\ny = {int(res.x[1])}\nvalor = {int(abs(res.fun))}", 
             xy=(70, 90), xycoords='data',
             xytext=(20, -30), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2"))

plt.tight_layout()

plt.show()

