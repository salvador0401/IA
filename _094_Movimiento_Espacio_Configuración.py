##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la librería NumPy para operaciones numéricas
from collections import deque  # Importa la clase deque para una cola eficiente

# Definición de la clase del entorno
class Entorno:
    def __init__(self, tamaño_x, tamaño_y, obstáculos):
        self.tamaño_x = tamaño_x  # Tamaño del entorno en el eje X
        self.tamaño_y = tamaño_y  # Tamaño del entorno en el eje Y
        self.obstáculos = obstáculos  # Lista de coordenadas de obstáculos

    # Función para verificar si una coordenada está dentro del entorno y no está ocupada por un obstáculo
    def es_celda_libre(self, coordenada):
        x, y = coordenada
        return 0 <= x < self.tamaño_x and 0 <= y < self.tamaño_y and (x, y) not in self.obstáculos

# Función para encontrar un camino desde el punto de inicio hasta el punto de destino utilizando búsqueda en anchura
def encontrar_camino(entorno, inicio, destino):
    # Inicialización
    visitado = set()  # Conjunto de celdas visitadas
    cola = deque([(inicio, [])])  # Cola de celdas por visitar (cada elemento es una tupla (celda, camino))

    # Búsqueda en anchura
    while cola:
        celda_actual, camino_actual = cola.popleft()  # Obtener la celda actual y el camino hasta ella
        if celda_actual == destino:  # Si la celda actual es el destino, devolver el camino
            return camino_actual + [celda_actual]
        if celda_actual in visitado:  # Si la celda ya ha sido visitada, pasar a la siguiente iteración
            continue
        visitado.add(celda_actual)  # Marcar la celda como visitada
        # Generar las coordenadas de las celdas adyacentes
        adyacentes = [(celda_actual[0] + dx, celda_actual[1] + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        # Filtrar las celdas adyacentes que están dentro del entorno y no están ocupadas por obstáculos
        adyacentes_libres = [c for c in adyacentes if entorno.es_celda_libre(c)]
        # Agregar las celdas adyacentes a la cola con el camino actual más la celda adyacente
        for celda in adyacentes_libres:
            cola.append((celda, camino_actual + [celda]))

    # Si no se puede encontrar un camino, devolver None
    return None

# Definición del entorno (tamaño del entorno: 10x10, obstáculos en las celdas (2,2), (3,2) y (4,2))
entorno = Entorno(10, 10, [(2, 2), (3, 2), (4, 2)])

# Punto de inicio y destino
inicio = (1, 1)
destino = (8, 8)

# Encontrar un camino desde el punto de inicio hasta el punto de destino
camino = encontrar_camino(entorno, inicio, destino)

# Imprimir el camino encontrado
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se pudo encontrar un camino.")
