##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la librería NumPy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa la librería Matplotlib para visualización

# Parámetros
num_particulas = 1000  # Número de partículas utilizadas en el filtro de partículas
limite_mapa = 10  # Tamaño del mapa (en este caso, un cuadrado de 10x10)
num_pasos = 20  # Número de pasos de tiempo

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

# Función para visualizar el mapa y la trayectoria estimada del robot
def visualizar_mapa(particulas, trayectoria, mapa_real=None):
    plt.figure(figsize=(8, 6))  # Configura el tamaño de la figura
    plt.scatter(particulas[:, 0], particulas[:, 1], color='b', s=5, alpha=0.5)  # Dibuja las partículas en azul
    plt.plot(trayectoria[:, 0], trayectoria[:, 1], color='r', linewidth=2)  # Dibuja la trayectoria estimada en rojo
    if mapa_real is not None:
        plt.scatter(mapa_real[:, 0], mapa_real[:, 1], color='g', s=20, marker='x')  # Dibuja el mapa real (si está disponible) en verde
    plt.xlabel('X')  # Etiqueta del eje X
    plt.ylabel('Y')  # Etiqueta del eje Y
    plt.title('Mapa y trayectoria estimada del robot')  # Título de la gráfica
    plt.grid(True)  # Habilita la cuadrícula en la gráfica
    plt.axis('equal')  # Configura los ejes para que tengan la misma escala
    plt.show()  # Muestra la gráfica

# Inicialización: Generar partículas aleatorias uniformemente distribuidas en el área del mapa
particulas = generar_particulas(num_particulas, limite_mapa, limite_mapa)

# Inicializar trayectoria del robot
trayectoria = np.zeros((num_pasos, 2))

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

    # Actualizar la trayectoria del robot (usamos la posición promedio de las partículas)
    trayectoria[paso] = np.mean(particulas, axis=0)

# Visualizar el mapa y la trayectoria estimada del robot
visualizar_mapa(particulas, trayectoria)
