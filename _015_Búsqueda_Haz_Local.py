##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np

# Función de ejemplo (podría ser cualquier otra función)
def funcion_objetivo(x):
    return x**4 - 3 * x**3 + 2 * x**2 + x

# Algoritmo de Búsqueda de Haz Local (Hill Climbing)
def busqueda_haz_local(func_obj, x_inicial, paso, max_iter):
    x_actual = x_inicial
    
    for _ in range(max_iter):
        valor_actual = func_obj(x_actual)
        
        # Generar un vecino
        vecino = x_actual + np.random.uniform(-paso, paso)
        
        # Evaluar el vecino
        valor_vecino = func_obj(vecino)
        
        # Actualizar la solución si el vecino es mejor
        if valor_vecino < valor_actual:
            x_actual = vecino
    
    return x_actual, func_obj(x_actual)

# Parámetros
x_inicial = 2  # Punto inicial
paso = 0.1  # Tamaño del paso
max_iter = 1000  # Número máximo de iteraciones

# Ejecución del algoritmo
mejor_solucion, mejor_valor = busqueda_haz_local(funcion_objetivo, x_inicial, paso, max_iter)

print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la función en la mejor solución:", mejor_valor)
