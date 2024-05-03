##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import heapq  # Importa el módulo heapq, que proporciona estructuras de datos para manejar colas de prioridad

class Grafo:
    def __init__(self):#inicializamos la clase
        self.vertices = {}  # Inicializa un diccionario para almacenar los vértices y sus aristas

    def agregar_vertice(self, vertice):#creamos una funcion que pide contexto y el vertice a agregar
        if vertice not in self.vertices:# si no se ha creado la vertice se entra a la condicional
            self.vertices[vertice] = {}  # Agrega un vértice al grafo si no existe

    def agregar_arista(self, inicio, fin, costo):
        self.agregar_vertice(inicio)  # Asegura que los vértices de inicio y fin existan en el grafo
        self.agregar_vertice(fin)#ve si el fin esta presente
        self.vertices[inicio][fin] = costo  # Agrega una arista desde inicio a fin con un costo dado
        self.vertices[fin][inicio] = costo  # Añade la arista en ambas direcciones, ya que el grafo es no dirigido

    def costo_uniforme(self, inicio, destino):#funcion que pide el nodo de inicio y la meta
        cola_prioridad = [(0, inicio)]  # Inicializa una cola de prioridad con el nodo de inicio y un costo de 0
        visitados = set()  # Inicializa un conjunto para mantener los nodos visitados

        while cola_prioridad:  # Mientras haya elementos en la cola de prioridad
            costo, nodo = heapq.heappop(cola_prioridad)  # Extrae el nodo con el menor costo de la cola
            if nodo not in visitados:  # Si el nodo no ha sido visitado
                visitados.add(nodo)  # Marca el nodo como visitado
                if nodo == destino:  # Si el nodo actual es el destino
                    return costo  # Devuelve el costo acumulado hasta el nodo destino
                for vecino, costo_arista in self.vertices[nodo].items():  # Para cada vecino del nodo actual
                    if vecino not in visitados:  # Si el vecino no ha sido visitado
                        nuevo_costo = costo + costo_arista  # Calcula el nuevo costo acumulado
                        heapq.heappush(cola_prioridad, (nuevo_costo, vecino))  # Agrega el vecino a la cola con su nuevo costo

        return float('inf')  # Devuelve infinito si no se encontró un camino al destino

# Ejemplo de uso
grafo = Grafo()  # Crea un nuevo grafo
grafo.agregar_arista('A', 'B', 1)  # Agrega aristas al grafo
grafo.agregar_arista('A', 'C', 5)# Agrega aristas al grafo
grafo.agregar_arista('B', 'D', 3)# Agrega aristas al grafo
grafo.agregar_arista('C', 'D', 2)# Agrega aristas al grafo
grafo.agregar_arista('C', 'E', 6)# Agrega aristas al grafo
grafo.agregar_arista('D', 'E', 4)# Agrega aristas al grafo

costo = grafo.costo_uniforme('A', 'E')  # Realiza la búsqueda del camino de costo uniforme desde A hasta E
print("Costo mínimo de A a E:", costo)  # Imprime el costo mínimo encontrado
