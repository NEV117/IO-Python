from pulp import *

# Crea el problema de maximización
prob = LpProblem("Problema de Optimización", LpMaximize)

# Variables de decisión
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)
x3 = LpVariable("x3", lowBound=0)
x4 = LpVariable("x4", lowBound=0)
b = LpVariable("b", cat=LpBinary)

# Función objetivo
prob += 3000 * x1 + 2000 * x2 + (-1000) * x3 + 4000 * x4

# Restricciones
prob += x1 + x2 + x3 + x4 <= 10, "Capacidad de producción"
prob += 4 * x1 - 2 * x2 + 2 * x3 + x4 <= 8, "Restricciones económicas"
prob += x1 + x2 + x3 + x4 >= 5, "Demanda mínima"
prob += x1 + x2 + 2 * x3 + x4 == 6, "Relaciones específicas de producción"
prob += x1 + x2 + x3 + x4 <= 2 * b, "Restricción de utilización de la máquina especializada"

# Restricciones adicionales para evitar valores negativos
prob += x1 >= 0, "No negatividad de x1"
prob += x2 >= 0, "No negatividad de x2"
prob += x3 >= 0, "No negatividad de x3"
prob += x4 >= 0, "No negatividad de x4"

# Resuelve el problema
prob.solve()

# Imprime el estado de la solución
print("Estado de la solución:", LpStatus[prob.status])

# Imprime el valor óptimo de las variables de decisión
print("Cantidad de aluminio producida (x1):", value(x1))
print("Cantidad de cobre producida (x2):", value(x2))
print("Cantidad de hierro producida (x3):", value(x3))
print("Cantidad de titanio producida (x4):", value(x4))
print("Variable binaria (b):", value(b))
