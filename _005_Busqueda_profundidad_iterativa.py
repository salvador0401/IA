##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def dfs_iterative(graph, start, goal, max_depth):# Definición de la función de búsqueda en profundidad iterativa
    for depth_limit in range(1, max_depth + 1):  # Iterar sobre los límites de profundidad desde 1 hasta max_depth
        result = dfs_limit(graph, start, goal, depth_limit)  # Realizar búsqueda en profundidad limitada con el límite de profundidad actual
        if result is not None:  # Si se encuentra un camino
            return result  # Devolver el camino encontrado
    return None  # Si no se encuentra un camino dentro de los límites de profundidad, devolver None

def dfs_limit(graph, start, goal, max_depth):# Definición de la función de búsqueda en profundidad limitada 
    visited = set()  # Conjunto para mantener un registro de nodos visitados
    stack = [(start, [start], 0)]  # Pila para realizar la búsqueda en profundidad con el nivel de profundidad
    while stack: # Mientras haya nodos en la pila
        node, path, depth = stack.pop()  # Sacar el nodo, el camino asociado y el nivel de profundidad de la pila
        if node not in visited:#si no se ha buscado en ese nodo entra
            if node == goal:#si el nodo es el que se requiere
                return path  # Si se encuentra el nodo objetivo, devolver el camino
            if depth < max_depth:  # Verificar el límite de profundidad
                visited.add(node)  # Marcar el nodo como visitado
                for neighbor in graph[node]:  # Iterar sobre los vecinos del nodo
                    stack.append((neighbor, path + [neighbor], depth + 1))  # Agregar vecinos a la pila con el nivel de profundidad actualizado
    return None  # Si no se encuentra un camino al objetivo dentro del límite de profundidad, devolver None

# Ejemplo de grafo
graph = {
    'A': ['B', 'C'],  # Nodo A tiene vecinos B y C
    'B': ['A', 'D', 'E'],  # Nodo B tiene vecinos A, D y E
    'C': ['A', 'F'],  # Nodo C tiene vecinos A y F
    'D': ['B'],  # Nodo D tiene vecino B
    'E': ['B', 'F'],  # Nodo E tiene vecinos B y F
    'F': ['C', 'E'],  # Nodo F tiene vecinos C y E
    'G': ['C', 'F', 'I'],#lo mismo
    'H': ['D'],#lo mismo
    'I': ['G', 'J'],#lo mismo
    'J': ['I']#lo mismo
}

start_node = 'A'  # Nodo de inicio
goal_node = 'I'   # Nodo objetivo
max_depth = 4  # Profundidad máxima permitida para cada iteración de la búsqueda en profundidad

print("Camino encontrado:", dfs_iterative(graph, start_node, goal_node, max_depth))# Realizar búsqueda en profundidad iterativa e imprimir el camino encontrado
