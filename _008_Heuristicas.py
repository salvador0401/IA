##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import heapq  # Importamos el módulo heapq para usar colas de prioridad

# Definición de la estructura del grafo como un diccionario
grafo = {
    'A': {'B': 5, 'C': 10},  # Desde el nodo 'A' se puede ir a 'B' con peso 5 y a 'C' con peso 10
    'B': {'D': 15, 'E': 20},  # Desde 'B' se puede ir a 'D' con peso 15 y a 'E' con peso 20
    'C': {'F': 25},  # Desde 'C' se puede ir a 'F' con peso 25
    'D': {},  # 'D' no tiene vecinos
    'E': {'F': 30},  # Desde 'E' se puede ir a 'F' con peso 30
    'F': {}  # 'F' no tiene vecinos
}

# Función de búsqueda primero el mejor
def busqueda_primero_el_mejor(grafo, inicio, objetivo):
    frontera = []  # Creamos una cola de prioridad vacía para almacenar los nodos a expandir
    heapq.heappush(frontera, (0, [inicio]))  # Insertamos el nodo inicial en la cola de prioridad con una heurística inicial de 0 y un camino que solo contiene el nodo inicial
    visitados = set()  # Creamos un conjunto para almacenar los nodos visitados

    while frontera:  # Mientras haya nodos en la frontera para explorar
        _, camino_actual = heapq.heappop(frontera)  # Extraemos el nodo con menor heurística de la frontera
        nodo_actual = camino_actual[-1]  # Obtenemos el nodo actual del camino

        if nodo_actual == objetivo:  # Si hemos llegado al nodo objetivo
            return camino_actual  # Devolvemos el camino hasta el objetivo

        visitados.add(nodo_actual)  # Marcamos el nodo actual como visitado

        for vecino, peso in grafo[nodo_actual].items():  # Iteramos sobre los vecinos del nodo actual
            if vecino not in visitados:  # Si el vecino no ha sido visitado
                nuevo_camino = list(camino_actual)  # Creamos un nuevo camino que es una copia del camino actual
                nuevo_camino.append(vecino)  # Agregamos el vecino al nuevo camino
                valor_heuristico = peso  # La heurística en este caso es el peso del arco hasta el vecino
                heapq.heappush(frontera, (valor_heuristico, nuevo_camino))  # Insertamos el nuevo camino en la frontera con su heurística correspondiente

    return None  # Si no se encuentra un camino al objetivo, devolvemos None

# Ejemplo de uso
inicio = 'A'  # Nodo inicial
objetivo = 'F'  # Nodo objetivo

camino = busqueda_primero_el_mejor(grafo, inicio, objetivo)  # Realizamos la búsqueda del camino
if camino:
    print("Se encontró un camino al objetivo:", camino)  # Si se encuentra un camino, lo imprimimos
else:
    print("No se encontró un camino al objetivo.")  # Si no se encuentra un camino, mostramos un mensaje indicando que no se encontró
