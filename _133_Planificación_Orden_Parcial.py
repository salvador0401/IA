##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from collections import defaultdict  # Importar la clase defaultdict para crear diccionarios con valores predeterminados

class Task:  # Definir la clase Task para representar una tarea
    def __init__(self, name, duration):  # Método para inicializar una tarea con un nombre y una duración
        self.name = name  # Nombre de la tarea
        self.duration = duration  # Duración de la tarea

class PartialOrderPlanner:  # Definir la clase PartialOrderPlanner para el planificador de orden parcial
    def __init__(self):  # Método para inicializar el planificador
        self.order_constraints = defaultdict(list)  # Diccionario para almacenar las restricciones de orden entre tareas

    def add_order_constraint(self, before, after):  # Método para añadir una restricción de orden entre dos tareas
        self.order_constraints[after].append(before)  # Añadir la tarea 'before' como tarea anterior a la tarea 'after'

    def plan(self, tasks):  # Método para planificar las tareas
        planned = set()  # Conjunto para almacenar las tareas ya planificadas
        total_duration = 0  # Inicializar la duración total del plan a 0
        while len(planned) < len(tasks):  # Mientras queden tareas por planificar
            for task in tasks:  # Para cada tarea en la lista de tareas
                if task in planned:  # Si la tarea ya está planificada, continuar con la siguiente tarea
                    continue
                if all(pre in planned for pre in self.order_constraints[task]):  # Si todas las tareas previas están planificadas
                    planned.add(task)  # Planificar la tarea actual
                    total_duration += task.duration  # Añadir la duración de la tarea actual a la duración total
                    yield task, total_duration  # Devolver la tarea planificada y la duración total

# Crear un planificador de orden parcial
planner = PartialOrderPlanner()

# Definir las tareas y las restricciones de orden entre ellas
task_A = Task('A', 2)
task_B = Task('B', 3)
task_C = Task('C', 4)
task_D = Task('D', 2)
task_E = Task('E', 3)

planner.add_order_constraint(task_A, task_B)
planner.add_order_constraint(task_B, task_C)
planner.add_order_constraint(task_C, task_D)
planner.add_order_constraint(task_C, task_E)

# Planificar las tareas
tasks = [task_A, task_B, task_C, task_D, task_E]
plan = planner.plan(tasks)

# Imprimir el plan
print("El plan es:")
for task, total_duration in plan:  # Para cada tarea y su duración total en el plan
    print(f"Tarea: {task.name}, Duración acumulada: {total_duration}")  # Imprimir el nombre de la tarea y su duración acumulada
