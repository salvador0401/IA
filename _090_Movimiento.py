##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np
import time

# Función para imprimir la cuadrícula
def imprimir_cuadricula(cuadricula):
    for fila in cuadricula:
        print(' '.join(fila))

# Función para simular el movimiento en la cuadrícula
def simular_movimiento(cuadricula):
    # Generar nueva cuadrícula para el siguiente paso
    nueva_cuadricula = np.full_like(cuadricula, ' ')
    
    # Iterar sobre cada celda en la cuadrícula
    for i in range(len(cuadricula)):
        for j in range(len(cuadricula[0])):
            # Simular movimiento
            # Por ejemplo, mover un objeto representado por 'X' a la derecha
            if cuadricula[i][j] == 'X':
                nueva_posicion = (i, j + 1)
                # Verificar si la nueva posición está dentro de la cuadrícula
                if 0 <= nueva_posicion[1] < len(cuadricula[0]):
                    nueva_cuadricula[nueva_posicion] = 'X'
    
    return nueva_cuadricula

# Tamaño de la cuadrícula
filas = 5
columnas = 10

# Crear cuadrícula inicial con un objeto 'X'
cuadricula = np.full((filas, columnas), ' ')
cuadricula[2][2] = 'X'

# Iterar para simular el movimiento en la cuadrícula
for _ in range(5):
    imprimir_cuadricula(cuadricula)
    print('-' * (columnas * 2))
    cuadricula = simular_movimiento(cuadricula)
    time.sleep(1)  # Esperar un segundo entre cada paso
