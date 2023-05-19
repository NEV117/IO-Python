from pulp import *

# Crear el problema de maximización
prob = LpProblem("Planificacion_de_Produccion", LpMaximize)

# Variables de decisión
X1 = LpVariable("X1", lowBound=0, cat='Integer')  # Cantidad de unidades de A producidas
X2 = LpVariable("X2", lowBound=0, cat='Integer')  # Cantidad de unidades de B producidas
X3 = LpVariable("X3", lowBound=0, cat='Integer')  # Cantidad de unidades de C producidas
X4 = LpVariable("X4", cat='Binary')              # Variable binaria

# Función objetivo
prob += 10*X1 + 8*X2 + 12*X3, "Beneficio_total"

# Restricciones
prob += X1 >= 100, "Restriccion_prod_A"
prob += X2 >= 150, "Restriccion_prod_B"
prob += X1 + X2 >= 200*X4, "Restriccion_utilizacion_maquina"
prob += X1 + X2 + X3 <= 500, "Restriccion_prod_max_total"

# Resolver el problema
prob.solve()

# Imprimir el estado de la solución
print("Estado de la solución:", LpStatus[prob.status])

# Imprimir la cantidad óptima de cada producto
print("Cantidad óptima de unidades de A:", value(X1))
print("Cantidad óptima de unidades de B:", value(X2))
print("Cantidad óptima de unidades de C:", value(X3))

# Imprimir si se utiliza o no la máquina especializada
if value(X4) == 1:
    print("Se utiliza la máquina especializada.")
else:
    print("No se utiliza la máquina especializada.")

# Imprimir el beneficio total máximo
print("Beneficio total máximo: $", value(prob.objective))
