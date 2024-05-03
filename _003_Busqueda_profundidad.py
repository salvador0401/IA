##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def dfs(graph, start, goal):#definimos la funcion dfs la cual pide de datos el grafo a usar, el inicio de la busqueda y adonde se quiere llegar
    visited = set()# Conjunto para mantener un registro de nodos visitados
    stack = [(start, [start])] # Pila para realizar la búsqueda en profundidad
    while stack:# Mientras haya nodos en la pila
        (node, path) = stack.pop()# Sacar el nodo y el camino asociado de la pila
        if node not in visited:# Si el nodo no ha sido visitado   
            if node == goal:# Si el nodo es el objetivo, devolver el camino
                return path
            
            visited.add(node)# Marcar el nodo como visitado
           
            for neighbor in graph[node]: # Agregar los vecinos del nodo a la pila con el camino actualizado
                stack.append((neighbor, path + [neighbor]))
    return None# Si no se encuentra un camino al objetivo, devolver None

graph = {#creamos un grafo
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'#incio de la busqueda
goal_node = 'F'#meta de la busqueda

# Imprimir el camino encontrado por la búsqueda en profundidad
print("Camino encontrado:", dfs(graph, start_node, goal_node))#imprimimos el resultado el cual es llamado ahi mismo a la funcion dfs y le pasasmos lo parametros requeridos
