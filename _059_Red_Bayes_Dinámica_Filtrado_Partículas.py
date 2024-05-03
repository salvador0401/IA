##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importamos la biblioteca NumPy para operaciones matriciales

class FiltroParticulas:
    def __init__(self, num_particulas, limite_superior):
        self.num_particulas = num_particulas  # Número de partículas
        self.limite_superior = limite_superior  # Límite superior del espacio de estado
        # Inicializamos las partículas aleatorias uniformemente en el intervalo [0, limite_superior)
        self.particulas = np.random.uniform(0, limite_superior, num_particulas)
        # Inicializamos los pesos de las partículas uniformemente
        self.weights = np.ones(num_particulas) / num_particulas

    def predecir(self, movimiento):
        # Movemos las partículas según el modelo de movimiento (aquí, solo se suma el movimiento)
        self.particulas += movimiento
        # Manejamos el desbordamiento del límite superior del espacio de estado
        self.particulas %= self.limite_superior

    def actualizar(self, observacion, varianza_sensor):
        # Calculamos la probabilidad de la observación para cada partícula usando una distribución Gaussiana
        likelihoods = 1 / np.sqrt(2 * np.pi * varianza_sensor) * np.exp(-0.5 * ((observacion - self.particulas) ** 2) / varianza_sensor)
        # Actualizamos los pesos multiplicando por la probabilidad de la observación
        self.weights *= likelihoods
        # Normalizamos los pesos para que sumen 1
        self.weights /= np.sum(self.weights)

    def reponderar(self):
        # Resampleamos las partículas basadas en sus pesos
        indices = np.random.choice(np.arange(self.num_particulas), size=self.num_particulas, p=self.weights)
        self.particulas = self.particulas[indices]
        self.weights = np.ones(self.num_particulas) / self.num_particulas

    def estimar_estado(self):
        # Estimamos el estado utilizando la media de las partículas ponderadas por sus pesos
        estado_estimado = np.sum(self.particulas * self.weights)
        return estado_estimado

# Parámetros del filtro de partículas
num_particulas = 1000  # Número de partículas
limite_superior = 10  # Límite superior del espacio de estado
varianza_sensor = 0.1  # Varianza del sensor

# Crear el filtro de partículas
filtro = FiltroParticulas(num_particulas, limite_superior)

# Simulación
movimientos = np.random.normal(1, 0.5, 100)  # Generar movimientos aleatorios
# Generar observaciones ruidosas (en este caso, una señal sinusoidal con ruido gaussiano)
observaciones_verdaderas = np.sin(np.linspace(0, 2*np.pi, 100)) + np.random.normal(0, np.sqrt(varianza_sensor), 100)

# Actualizar el filtro de partículas y estimar el estado en cada paso de tiempo
for movimiento, observacion in zip(movimientos, observaciones_verdaderas):
    filtro.predecir(movimiento)  # Predicción del estado futuro basada en el modelo de movimiento
    filtro.actualizar(observacion, varianza_sensor)  # Actualización basada en la observación actual
    filtro.reponderar()  # Reponderación de las partículas basada en los pesos actualizados
    estado_estimado = filtro.estimar_estado()  # Estimación del estado basada en las partículas y pesos
    print("Estado estimado:", estado_estimado)  # Imprimir la estimación del estado en cada paso de tiempo
