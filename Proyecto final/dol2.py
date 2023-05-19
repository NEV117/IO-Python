from pulp import *

# Crear el problema de maximización
prob = LpProblem("Problema", LpMaximize)

# Definir las variables de decisión
x1 = LpVariable("x1", lowBound=0, cat='Continuous')
x2 = LpVariable("x2", lowBound=0, cat='Continuous')
x3 = LpVariable("x3", lowBound=0, cat='Continuous')
x4 = LpVariable("x4", lowBound=0, upBound=1, cat='Binary')

# Definir la función objetivo
prob += 3*x1 + 2*x2 - x3 + 4*x4, "Z"

# Definir las restricciones
prob += 2*x1 + 3*x2 - x3 + 2*x4 <= 10, "Restricción 1"
prob += 4*x1 - 2*x2 + 2*x3 + x4 <= 8, "Restricción 2"
prob += x1 + x2 + x3 + x4 >= 5, "Restricción 3"
prob += x1 + x2 + 2*x3 + x4 == 6, "Restricción 4"

# Resolver el problema
prob.solve()

# Imprimir el estado de la solución
print("Estado:", LpStatus[prob.status])

# Imprimir el valor óptimo de la función objetivo
print("Valor óptimo de Z =", value(prob.objective))

# Imprimir los valores óptimos de las variables de decisión
for v in prob.variables():
    print(v.name, "=", v.varValue)
