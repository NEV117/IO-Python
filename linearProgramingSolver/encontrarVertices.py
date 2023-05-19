from sympy import symbols, Eq, Interval, solve

x, y = symbols('x y')

# definir las restricciones
rest1 = Eq(2 * x + y, 230)
rest2 = Eq(x + 2 * y, 250)
rest3 = Eq(x, 0)
rest4 = Eq(y, 0)
rest5 = Eq(y, 120)

# resolver el sistema de ecuaciones para cada vértice
sol1 = solve((rest1, rest3, rest4), (x, y))
sol2 = solve((rest1, rest2, rest4), (x, y))
sol3 = solve((rest1, rest2, rest5), (x, y))
sol4 = solve((rest2, rest5, rest3), (x, y))

# imprimir los vértices de la zona factible
print(sol1)
print(sol2)
print(sol3)
print(sol4)
