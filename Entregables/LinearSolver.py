import numpy as np #pip install numpy
from scipy.optimize import linprog #pip install scipy
#Nicolas Escandon Varela 2205629

#Las variables estan en ingles porque me acostumbre a nombrar asi

#Funcion que lo resuelve
def solve_lp(c, A, b, bounds, optimize_for='maximizar'):
    #Si se seleeciona maximizar va a negar los coeficientes de la funcion objetivo
    #Necesita hacer esto porque asi entiende la libreria que debe hacer
    if optimize_for == 'maximizar':
        c = [-x for x in c] 

    #Se le pasan a la libreria las variables
    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

    #Si se encuentra una solucion imprime un mensaje    
    if res.success == True:
        print('\n\n----------------------------Optimización terminada con éxito.----------------------------')
        print("La solución (x1, x2, ..., xn) es:")
        print(res.x)
        print('El valor óptimo es:')
        print(abs(res.fun))

    else:
        print('Sin solución :C')

    
#Inputs de los datos abajo
c = [int(x) for x in input("Ingrese los coeficientes de la función objetivo (separados por espacio): ").split()]
A = []

num_constraints = int(input("Ingrese el número de restricciones: "))
for i in range(num_constraints):
    constraint = [float(x) for x in input(f"Ingrese los coeficientes de la restricción {i + 1} (separados por espacio): ").split()]
    A.append(constraint)

b = [int(x) for x in input("Ingrese los límites de las restricciones (separados por espacio): ").split()]
bounds = []

num_variables = int(input("Ingrese el número de variables: "))
for i in range(num_variables):
    lower_bound = int(input(f"Ingrese el límite inferior de la variable {i + 1}: "))
    upper_bound = input(f"Ingrese el límite superior de la variable {i + 1} (presione enter si no existe): ")
    if upper_bound == '':
        upper_bound = None
    else:
        upper_bound = int(upper_bound)
    bounds.append((lower_bound, upper_bound))

optimize_for = input("Desea maximizar o minimizar? ").lower()

#Llamado a la funcion
solve_lp(c, A, b, bounds, optimize_for)
