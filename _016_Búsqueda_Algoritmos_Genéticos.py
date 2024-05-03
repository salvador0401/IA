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

# Lista de ubicaciones de correos electrónicos (podría ser cualquier otro conjunto de ubicaciones)
correos = [(2, 3), (5, 7), (8, 1), (9, 6), (3, 9), (6, 2)]

# Función para calcular la distancia entre dos ubicaciones (en este caso, usamos la distancia euclidiana)
def distancia(ubicacion1, ubicacion2):
    # Calcula la distancia euclidiana entre dos ubicaciones
    return np.sqrt((ubicacion1[0] - ubicacion2[0])**2 + (ubicacion1[1] - ubicacion2[1])**2)

# Función de fitness: número de correos entregados en una ruta
def fitness(ruta):
    # Inicializa el contador de correos entregados
    correos_entregados = 0
    # Itera sobre la longitud de la ruta
    for i in range(len(ruta) - 1):
        # Calcula la distancia entre los correos en la ruta
        distancia_entre_correos = distancia(correos[ruta[i]], correos[ruta[i+1]])
        # Supongamos que se entrega un correo en cada ubicación, por lo que se incrementa el contador
        correos_entregados += 1
    return correos_entregados

# Algoritmo genético
def algoritmo_genetico(tam_poblacion, tam_ruta, num_generaciones):
    # Inicializa la población con permutaciones aleatorias de las ubicaciones de los correos
    poblacion = np.zeros((tam_poblacion, tam_ruta), dtype=int)
    for i in range(tam_poblacion):
        poblacion[i] = np.random.permutation(tam_ruta)
    # Inicializa la mejor solución y su fitness como nulo y menos infinito, respectivamente
    mejor_solucion = None
    mejor_fitness = float('-inf')
    
    # Itera sobre el número de generaciones especificado
    for _ in range(num_generaciones):
        # Calcula el fitness de toda la población
        fitness_poblacion = [fitness(individuo) for individuo in poblacion]
        # Encuentra el índice del individuo con el mejor fitness
        idx_mejor = np.argmax(fitness_poblacion)
        # Actualiza la mejor solución y su fitness si se encuentra un mejor individuo
        if fitness_poblacion[idx_mejor] > mejor_fitness:
            mejor_fitness = fitness_poblacion[idx_mejor]
            mejor_solucion = poblacion[idx_mejor]
        
        # Realiza la selección de padres y el cruce para generar la descendencia
        padres = seleccion_padres(poblacion, fitness_poblacion)
        descendencia = []
        for i in range(0, tam_poblacion, 2):
            hijo1, hijo2 = cruce(padres[i], padres[i+1])
            descendencia.append(hijo1)
            descendencia.append(hijo2)
        
        # Actualiza la población con la nueva descendencia
        poblacion = np.array(descendencia)
    
    return mejor_solucion, mejor_fitness

# Función de selección de padres: selección por torneo
def seleccion_padres(poblacion, fitness_poblacion):
    # Inicializa la lista de padres
    padres = []
    # Itera sobre toda la población para seleccionar padres
    for _ in range(len(poblacion)):
        # Selecciona dos individuos al azar
        idx1 = np.random.randint(0, len(poblacion))
        idx2 = np.random.randint(0, len(poblacion))
        # Agrega el individuo con el mejor fitness como padre
        if fitness_poblacion[idx1] > fitness_poblacion[idx2]:
            padres.append(poblacion[idx1])
        else:
            padres.append(poblacion[idx2])
    return padres

# Función de cruce: cruce en un punto
def cruce(padre1, padre2):
    # Elije un punto de cruce aleatorio
    punto_cruce = np.random.randint(1, len(padre1))
    # Realiza el cruce de los padres en el punto de cruce para generar dos hijos
    hijo1 = np.concatenate((padre1[:punto_cruce], padre2[punto_cruce:]))
    hijo2 = np.concatenate((padre2[:punto_cruce], padre1[punto_cruce:]))
    return hijo1, hijo2

# Parámetros del algoritmo genético
tam_poblacion = 50
tam_ruta = len(correos)
num_generaciones = 100

# Ejecución del algoritmo genético
mejor_solucion, mejor_fitness = algoritmo_genetico(tam_poblacion, tam_ruta, num_generaciones)

# Imprime el resultado
print("Mejor ruta encontrada:", mejor_solucion)
print("Número de correos entregados en la mejor ruta:", mejor_fitness)

