##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def dfs_limit(graph, start, goal, max_depth):#definimos la funcion
    # Definición de la función de búsqueda en profundidad limitada
    # graph: el grafo representado como un diccionario donde las claves son los nodos y los valores son listas de nodos vecinos
    # start: el nodo de inicio desde donde comienza la búsqueda
    # goal: el nodo objetivo que se busca alcanzar
    # max_depth: la profundidad máxima permitida para la búsqueda
    visited = set()  # Conjunto para mantener un registro de nodos visitados
    stack = [(start, [start], 0)]  # Pila para realizar la búsqueda en profundidad con el nivel de profundidad
    while stack:#mientras se tengan restantes a buscar,
        # Mientras haya nodos en la pila
        node, path, depth = stack.pop()  # Sacar el nodo, el camino asociado y el nivel de profundidad de la pila
        if node not in visited:#si no se ha buscado en ese nodo
            if node == goal:# Si se encuentra el nodo objetivo,
                return path  #devolver el camino
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
    'F': ['C', 'E']  # Nodo F tiene vecinos C y E
}

start_node = 'A'  # Nodo de inicio
goal_node = 'F'   # Nodo objetivo
max_depth = 2  # Profundidad máxima permitida
print("Camino encontrado:", dfs_limit(graph, start_node, goal_node, max_depth))# Imprimir el camino encontrado por la búsqueda en profundidad limitada
