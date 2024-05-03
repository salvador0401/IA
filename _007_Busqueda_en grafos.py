##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from collections import defaultdict, deque# Importamos el módulo 'defaultdict' de la librería 'collections' y el módulo 'deque' de la misma librería

# Definimos una clase llamada 'Grafo'
class Grafo:
    # Método inicializador de la clase
    def __init__(self):
        # Creamos un diccionario para almacenar las listas de adyacencia de los nodos del grafo
        self.grafo = defaultdict(list)

    # Método para agregar una arista al grafo
    def agregar_arista(self, u, v):
        # Añadimos el nodo 'v' a la lista de adyacencia del nodo 'u'
        self.grafo[u].append(v)

    # Método para realizar búsqueda en amplitud (BFS)
    def bfs(self, inicio, objetivo):
        # Creamos un conjunto para almacenar los nodos visitados
        visitado = set()
        # Creamos una cola para almacenar los nodos que se van a visitar
        cola = deque()

        # Agregamos el nodo inicial a la cola y lo marcamos como visitado
        cola.append(inicio)
        visitado.add(inicio)

        # Mientras haya nodos en la cola
        while cola:
            # Sacamos el primer nodo de la cola
            nodo_actual = cola.popleft()
            # Imprimimos el nodo que estamos visitando en este momento
            print("Visitando nodo:", nodo_actual)

            # Si el nodo actual es el objetivo, terminamos la búsqueda
            if nodo_actual == objetivo:
                print("¡Objetivo encontrado!")
                return True

            # Exploramos los nodos vecinos del nodo actual
            for vecino in self.grafo[nodo_actual]:
                # Si el vecino no ha sido visitado, lo agregamos a la cola y lo marcamos como visitado
                if vecino not in visitado:
                    cola.append(vecino)
                    visitado.add(vecino)

        # Si llegamos aquí, no se encontró el objetivo
        print("No se encontró el objetivo.")
        return False

# Ejemplo de uso
# Creamos un objeto de la clase Grafo
g = Grafo()
# Agregamos algunas aristas al grafo
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(1, 2)
g.agregar_arista(2, 0)
g.agregar_arista(2, 3)
g.agregar_arista(3, 3)

# Definimos el nodo inicial y el nodo objetivo
inicio = 2
objetivo = 3

# Imprimimos un mensaje indicando que se realizará la búsqueda BFS
print("Búsqueda BFS:")
# Llamamos al método bfs para realizar la búsqueda en el grafo
g.bfs(inicio, objetivo)
