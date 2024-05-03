##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from collections import deque  # Importa la clase deque de la biblioteca collections
class Grafo:  # Definición de la clase Grafo
    def __init__(self):  # Constructor de la clase Grafo
        self.vertices = {}  # Inicializa un diccionario para almacenar los vértices y sus aristas
    
    def agregar_vertice(self, vertice):  # Método para agregar un vértice al grafo
        if vertice not in self.vertices:  # Verifica si el vértice no está en el grafo
            self.vertices[vertice] = []  # Si no está, lo agrega al diccionario con una lista vacía de aristas
    
    def agregar_arista(self, vertice1, vertice2):  # Método para agregar una arista entre dos vértices
        if vertice1 in self.vertices and vertice2 in self.vertices:  # Verifica si ambos vértices existen en el grafo
            self.vertices[vertice1].append(vertice2)  # Agrega el vértice2 a la lista de aristas del vértice1
            self.vertices[vertice2].append(vertice1)  # Agrega el vértice1 a la lista de aristas del vértice2
    
    def bfs(self, inicio, objetivo):  # Método de búsqueda en amplitud (BFS) en el grafo
        if inicio not in self.vertices or objetivo not in self.vertices:  # Verifica si los vértices dados existen en el grafo
            return None  # Si alguno de los vértices no existe, devuelve None
        
        visitados = set()  # Conjunto para almacenar los nodos visitados
        cola = deque()  # Crea una cola usando la clase deque
        cola.append((inicio, [inicio]))  # Agrega la tupla (inicio, [inicio]) a la cola
        
        while cola:  # Mientras la cola no esté vacía
            nodo_actual, camino = cola.popleft()  # Obtiene el nodo y el camino asociado de la cola
            visitados.add(nodo_actual)  # Marca el nodo como visitado
            if nodo_actual == objetivo:  # Si el nodo actual es el objetivo
                return camino  # Devuelve el camino hasta el objetivo
            
            for vecino in self.vertices[nodo_actual]:  # Para cada vecino del nodo actual
                if vecino not in visitados:  # Si el vecino no ha sido visitado
                    cola.append((vecino, camino + [vecino]))  # Agrega el vecino y su camino al final de la cola
                    visitados.add(vecino)  # Marca el vecino como visitado
        
        return None  # Si no se encuentra un camino, devuelve None

grafo = Grafo()  # Crea una instancia de la clase Grafo
grafo.agregar_vertice('A')# Agrega vértices al grafo
grafo.agregar_vertice('B')# Agrega vértices al grafo
grafo.agregar_vertice('C')# Agrega vértices al grafo
grafo.agregar_vertice('D')# Agrega vértices al grafo
grafo.agregar_vertice('E')# Agrega vértices al grafo
grafo.agregar_vertice('F')# Agrega vértices al grafo
grafo.agregar_vertice('G')# Agrega vértices al grafo
grafo.agregar_vertice('H')# Agrega vértices al grafo
grafo.agregar_vertice('I')# Agrega vértices al grafo
grafo.agregar_vertice('J')# Agrega vértices al grafo

grafo.agregar_arista('A', 'B')# Agrega aristas al grafo
grafo.agregar_arista('A', 'C')# Agrega aristas al grafo
grafo.agregar_arista('B', 'E')# Agrega aristas al grafo
grafo.agregar_arista('C', 'D')# Agrega aristas al grafo
grafo.agregar_arista('D', 'E')# Agrega aristas al grafo
grafo.agregar_arista('D', 'G')# Agrega aristas al grafo
grafo.agregar_arista('G', 'H')# Agrega aristas al grafo
grafo.agregar_arista('H', 'I')# Agrega aristas al grafo
grafo.agregar_arista('I', 'J')# Agrega aristas al grafo
grafo.agregar_arista('D', 'J')# Agrega aristas al grafo

inicio = 'A'  # Nodo inicial de la búsqueda
objetivo = 'I'  # Nodo objetivo de la búsqueda
camino = grafo.bfs(inicio, objetivo)  # Realiza una búsqueda en amplitud desde el nodo inicial al objetivo
if camino:  # Si se encontró un camino
    print(f"Se encontró un camino de {inicio} a {objetivo}: {' -> '.join(camino)}")  # Imprime el camino encontrado
else:  # Si no se encontró un camino
    print(f"No se encontró un camino de {inicio} a {objetivo}.")  # Imprime un mensaje de que no se encontró camino
 
