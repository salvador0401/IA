##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np

# Función para generar partículas aleatorias dentro del área del mapa
def generar_particulas(num_particulas, limite_x, limite_y):
    return np.random.uniform(low=(0, 0), high=(limite_x, limite_y), size=(num_particulas, 2))

# Función para simular la medición de distancia (en este caso, solo usamos la distancia al origen)
def medir_distancia(posicion):
    return np.linalg.norm(posicion, axis=1)

# Función para realizar el re-muestreo de las partículas basadas en las probabilidades de peso
def remuestrear(particulas, pesos):
    indices = np.random.choice(len(particulas), size=len(particulas), p=pesos)
    return particulas[indices]

# Parámetros
num_particulas = 1000
limite_mapa = 10
num_pasos = 10

# Inicialización: Generar partículas aleatorias uniformemente distribuidas en el área del mapa
particulas = generar_particulas(num_particulas, limite_mapa, limite_mapa)

for paso in range(num_pasos):
    # Movimiento: Simular el movimiento del robot (en este ejemplo, simplemente se agrega ruido gaussiano a las partículas)
    particulas += np.random.normal(loc=0, scale=0.5, size=particulas.shape)

    # Medición: Simular la obtención de observaciones (en este caso, solo la distancia al origen)
    medidas = medir_distancia(particulas)

    # Calcular pesos basados en las medidas (usamos la inversa de la distancia como una medida de similitud)
    pesos = 1 / medidas
    pesos /= np.sum(pesos)  # Normalizar los pesos para obtener una distribución de probabilidad

    # Re-muestreo: Actualizar las partículas basadas en los pesos
    particulas = remuestrear(particulas, pesos)

# Estimación final de la posición del robot (usamos el promedio de las partículas)
posicion_estimada = np.mean(particulas, axis=0)

print("Posición estimada del robot:", posicion_estimada)
