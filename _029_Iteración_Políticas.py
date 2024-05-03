##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np
# Definición del entorno
# Las filas representan estados y las columnas representan acciones
R = np.array([
    [-1, -3],  # Estado 0: Acción 0 -> Recompensa -1, Acción 1 -> Recompensa -3
    [-2, 10],  # Estado 1: Acción 0 -> Recompensa -2, Acción 1 -> Recompensa 10
])

# Matriz de transiciones de estado
# T[s, a, s'] representa la probabilidad de pasar al estado 's'' al tomar la acción 'a' desde el estado 's'
T = np.array([
    [[1, 0], [0, 1]],  # Desde el estado 0, Acción 0: 100% de probabilidad de permanecer en el estado 0
                       # Desde el estado 0, Acción 1: 100% de probabilidad de pasar al estado 1
    [[1, 0], [0, 1]]   # Desde el estado 1, Acción 0: 100% de probabilidad de permanecer en el estado 1
                       # Desde el estado 1, Acción 1: 100% de probabilidad de permanecer en el estado 1
])

# Definición de la política inicial
politica = np.ones((2, 2)) / 2  # 2 estados, 2 acciones

# Algoritmo de evaluación de política iterativa
def evaluacion_politica(politica, R, T, gamma=0.9, theta=0.0001):
    V = np.zeros(len(R))  # Inicializamos los valores de los estados a 0
    while True:  # Inicia un bucle que se ejecutará hasta que se cumpla una condición de convergencia
        delta = 0  # Inicializa el valor de cambio máximo entre las iteraciones
        for s in range(len(R)):  # Itera sobre cada estado en el problema
            v = V[s]  # Almacena el valor actual del estado
            # Calcula el nuevo valor del estado utilizando la política y las recompensas
            V[s] = sum(politica[s, a] * sum(T[s, a, s1] * (R[s, a] + gamma * V[s1]) for s1 in range(len(R))) for a in range(len(politica[s])))
            # Actualiza el valor de cambio máximo
            delta = max(delta, abs(v - V[s]))
        if delta < theta:  # Comprueba si se ha alcanzado la convergencia
            break  # Si el cambio es lo suficientemente pequeño, se detiene la iteración
    return V  # Devuelve los valores de los estados calculados

# Ejecutar el algoritmo de evaluación de política
valores = evaluacion_politica(politica, R, T)

print("Valores de los estados:")
print(valores)
