import numpy as np
import matplotlib.pyplot as plt

# Definir las funciones de restricción
def restriccion1(x1):
    return 230 - 2*x1

def restriccion2(x1):
    return (250 - x1)/2

def restriccion3(x1):
    return 0.8*x1 + 30

restricciones = [restriccion1, restriccion2, restriccion3] # lista de restricciones

# Calcular los valores de intersección
x1 = np.linspace(0, 125, 100)
intersecciones = np.minimum.reduce([r(x1) for r in restricciones])

# Crear la figura y el eje
fig, ax = plt.subplots()

# Agregar las líneas de restricción
for i, r in enumerate(restricciones):
    ax.plot(x1, r(x1), label=f'Restricción {i+1}')

# Sombrear la región que satisface todas las restricciones
ax.fill_between(x1, intersecciones, 0, where=intersecciones > 0, color='yellow')

# Establecer los límites de los ejes
ax.set_xlim([0, 130])
ax.set_ylim([0, 130])

# Agregar etiquetas de ejes y título
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_title('Área de solución para varias restricciones')

# Agregar leyenda
ax.legend()

# Mostrar la figura
plt.show()
