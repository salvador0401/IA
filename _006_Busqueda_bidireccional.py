##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def busqueda_bidireccional(grafo, inicio, objetivo):
    visitados_inicio = set()# Inicialización de los conjuntos de nodos visitados desde el inicio y el objetivo
    visitados_objetivo = set()# Inicialización de los conjuntos de nodos visitados desde el objetivo y el final
    
    
    frontera_inicio = [inicio]# Colas para los nodos frontera desde el inicio y el objetivo
    frontera_objetivo = [objetivo]# Colas para los nodos frontera desde el objetivo y el inicio
    
    while frontera_inicio and frontera_objetivo: # Bucle para la búsqueda bidireccional
        actual_inicio = frontera_inicio.pop(0)# Expansión desde el inicio
        visitados_inicio.add(actual_inicio)
        
        if actual_inicio in visitados_objetivo:# Comprobar si el nodo actual está en el conjunto de nodos visitados desde el objetivo
            return actual_inicio  # Si se encuentra, se ha encontrado una intersección y se devuelve el nodo
        
        actual_objetivo = frontera_objetivo.pop(0)# Expansión desde el objetivo
        visitados_objetivo.add(actual_objetivo)
        
        if actual_objetivo in visitados_inicio:# Comprobar si el nodo actual está en el conjunto de nodos visitados desde el inicio
            return actual_objetivo  # Si se encuentra, se ha encontrado una intersección y se devuelve el nodo
        
        for vecino in grafo[actual_inicio]:# Expandir los sucesores del nodo actual desde el inicio
            if vecino not in visitados_inicio and vecino not in frontera_inicio:
                frontera_inicio.append(vecino)
        
       
        for vecino in grafo[actual_objetivo]: # Expandir los sucesores del nodo actual desde el objetivo
            if vecino not in visitados_objetivo and vecino not in frontera_objetivo:
                frontera_objetivo.append(vecino)
    
    return None  # Si no se encuentra una intersección, devolver None

# creacion de grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

nodo_inicio = 'A'#grafo de inico
nodo_objetivo = 'F'#grafo meta

print("Nodo de intersección:", busqueda_bidireccional(grafo, nodo_inicio, nodo_objetivo))# Realizar búsqueda bidireccional e imprimir el nodo de intersección
