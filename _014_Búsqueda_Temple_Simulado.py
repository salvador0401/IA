##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Importación del módulo numpy como np
import numpy as np

# Matriz de adyacencia que representa las distancias entre puntos
distancias = np.array([[0, 2, 3, 0, 5],
                       [2, 0, 0, 0, 3],
                       [3, 0, 0, 0, 0],
                       [0, 0, 0, 0, 4],
                       [5, 3, 0, 4, 0]])

# Función para calcular la distancia total de una ruta
def distancia_total(ruta, distancias):
    # Inicializamos la distancia como 0
    distancia = 0
    # Iteramos sobre la longitud de la ruta
    for i in range(len(ruta) - 1):
        # Sumamos la distancia entre los puntos consecutivos de la ruta
        distancia += distancias[ruta[i]][ruta[i+1]]
    return distancia

# Implementación del algoritmo de Temple Simulado para búsqueda de rutas
def temple_simulado_busqueda_ruta(distancias, punto_inicio, punto_destino, temperatura_inicial, factor_enfriamiento, max_iter):
    # Inicializamos la mejor ruta y su distancia como la distancia directa entre el punto de inicio y destino
    mejor_ruta = [punto_inicio]
    mejor_distancia = distancias[punto_inicio][punto_destino]
    ruta_actual = mejor_ruta
    distancia_actual = mejor_distancia
    temperatura_actual = temperatura_inicial
    
    # Iteramos sobre el número máximo de iteraciones
    for _ in range(max_iter):
        # Generamos una permutación aleatoria de las intersecciones (excluyendo el punto de inicio y destino)
        intersecciones = list(range(1, len(distancias) - 1))
        np.random.shuffle(intersecciones)
        
        # Construimos la ruta incluyendo el punto de inicio y destino
        ruta_vecina = [punto_inicio] + intersecciones + [punto_destino]
        
        # Calculamos la distancia de la ruta vecina
        distancia_vecina = distancia_total(ruta_vecina, distancias)
        
        # Calculamos la diferencia entre la nueva distancia y la distancia actual
        diferencia = distancia_vecina - distancia_actual
        
        # Si la nueva distancia es mejor o aceptamos una peor distancia según la probabilidad de Boltzmann
        if diferencia < 0 or np.random.rand() < np.exp(-diferencia / temperatura_actual):
            ruta_actual = ruta_vecina
            distancia_actual = distancia_vecina
        
        # Actualizamos la mejor ruta si es necesario
        if distancia_actual < mejor_distancia:
            mejor_ruta = ruta_actual
            mejor_distancia = distancia_actual
        
        # Enfriamos la temperatura
        temperatura_actual *= factor_enfriamiento
    
    return mejor_ruta, mejor_distancia

# Parámetros
punto_inicio = 0
punto_destino = 4
temperatura_inicial = 100
factor_enfriamiento = 0.95
max_iter = 1000

# Ejecución del algoritmo
mejor_ruta, mejor_distancia = temple_simulado_busqueda_ruta(distancias, punto_inicio, punto_destino, temperatura_inicial, factor_enfriamiento, max_iter)

# Imprime el resultado
print("Mejor ruta encontrada:", mejor_ruta)
