##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from collections import deque  # Importar la clase deque para la implementación de la cola

class State:
    def __init__(self, x, y):  # Definir la clase State para representar un estado en la cuadrícula
        self.x = x  # Coordenada x del estado
        self.y = y  # Coordenada y del estado

    def __eq__(self, other):  # Método para verificar la igualdad de dos estados
        return self.x == other.x and self.y == other.y

    def __hash__(self):  # Método para calcular el hash de un estado (necesario para usarlo en conjuntos)
        return hash((self.x, self.y))

class Problem:
    def __init__(self, initial_state, goal_state):  # Definir la clase Problem para representar el problema de planificación
        self.initial_state = initial_state  # Estado inicial del problema
        self.goal_state = goal_state  # Estado objetivo del problema

    def actions(self, state):  # Método para obtener las acciones posibles desde un estado dado
        possible_actions = []  # Lista para almacenar las acciones posibles
        possible_actions.append(State(state.x + 1, state.y))  # Mover hacia la derecha
        possible_actions.append(State(state.x - 1, state.y))  # Mover hacia la izquierda
        possible_actions.append(State(state.x, state.y + 1))  # Mover hacia arriba
        possible_actions.append(State(state.x, state.y - 1))  # Mover hacia abajo
        possible_actions = [action for action in possible_actions if 0 <= action.x < 5 and 0 <= action.y < 5]  # Filtrar acciones para evitar salir de la cuadrícula
        return possible_actions

    def goal_test(self, state):  # Método para verificar si un estado es el estado objetivo
        return state == self.goal_state

def bfs(problem):  # Implementación del algoritmo de búsqueda en anchura
    frontier = deque()  # Declarar la cola para almacenar los estados que deben ser explorados
    explored = set()  # Declarar el conjunto para almacenar los estados ya explorados
    frontier.append((problem.initial_state, []))  # Agregar el estado inicial y una lista vacía para el camino al estado inicial en la cola
    while frontier:  # Mientras haya estados en la cola
        current_state, path = frontier.popleft()  # Obtener el estado actual y el camino actual desde la cola
        if problem.goal_test(current_state):  # Si el estado actual es el estado objetivo
            return path + [current_state]  # Devolver el camino al estado objetivo
        explored.add(current_state)  # Agregar el estado actual a los estados explorados
        for action in problem.actions(current_state):  # Para cada acción posible desde el estado actual
            if action not in explored and (action, path + [current_state]) not in frontier:  # Si la acción no ha sido explorada ni está en la cola
                frontier.append((action, path + [current_state]))  # Agregar la acción y el camino actualizado a la cola
    return None  # Devolver None si no se encuentra una solución

def print_solution(solution):  # Función para imprimir la solución encontrada
    if solution is None:  # Si no se encontró una solución
        print("No se encontró una solución.")
    else:  # Si se encontró una solución
        print("La solución encontrada es:")
        for state in solution:  # Para cada estado en la solución
            print("({}, {})".format(state.x, state.y))  # Imprimir las coordenadas del estado

initial_state = State(0, 0)  # Definir el estado inicial
goal_state = State(4, 4)  # Definir el estado objetivo
problem = Problem(initial_state, goal_state)  # Definir el problema de planificación

solution = bfs(problem)  # Encontrar la solución utilizando BFS
print_solution(solution)  # Imprimir la solución encontrada
