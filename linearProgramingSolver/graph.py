import matplotlib.pyplot as plt #pip install matplotlib
import numpy as np #pip install scipy


vertices = [(0, 120), (10, 120), (55,120), (70, 90), (115, 0), (0,0)]
xx = [v[0] for v in vertices]
yy = [v[1] for v in vertices]



x = np.linspace(0, 115, 100)
y1 = 230 - 2 * x
y2 = 250 - x
y3 = 120 * np.ones_like(x)


plt.plot(x, y1, label='2x + y <= 230')
plt.plot(x, y2, label='x + 2y <= 250')
plt.plot(x, y3, label='y <= 120')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.fill(xx, yy, 'cyan')
plt.axis('equal')

# Este punto verde representa la solucion  del problema de programacion lineal
plt.scatter(70, 90, color='green', s=50) 

plt.tight_layout()

plt.show()
