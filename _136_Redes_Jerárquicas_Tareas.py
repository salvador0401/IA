##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Task:
    def __init__(self, name, subtasks=None):  # Define la clase Task con un constructor que recibe el nombre de la tarea y una lista opcional de sub tareas
        self.name = name  # Asigna el nombre de la tarea al atributo name
        self.subtasks = subtasks if subtasks else []  # Asigna la lista de sub tareas al atributo subtasks, o crea una lista vacía si no se proporciona ninguna

    def add_subtask(self, subtask):  # Método para agregar una sub tarea a la lista de sub tareas
        self.subtasks.append(subtask)  # Agrega la sub tarea a la lista de sub tareas de la tarea actual

    def __repr__(self):  # Método especial para representar la tarea como una cadena
        return f"Task({self.name}, {self.subtasks})"  # Retorna una cadena que representa la tarea y sus sub tareas

def execute_task(task):  # Función para ejecutar una tarea y sus sub tareas recursivamente
    print(f"Ejecutando tarea: {task.name}")  # Imprime el nombre de la tarea actual
    for subtask in task.subtasks:  # Itera sobre todas las sub tareas de la tarea actual
        execute_task(subtask)  # Llama recursivamente a execute_task para ejecutar la sub tarea

# Ejemplo de uso
if __name__ == "__main__":
    tarea_principal = Task("Tarea Principal")  # Crea una tarea principal con el nombre "Tarea Principal"
    sub_tarea1 = Task("Subtarea 1")  # Crea una sub tarea con el nombre "Subtarea 1"
    sub_tarea2 = Task("Subtarea 2")  # Crea otra sub tarea con el nombre "Subtarea 2"
    sub_sub_tarea1 = Task("Sub-Subtarea 1")  # Crea una sub sub tarea con el nombre "Sub-Subtarea 1"
    sub_sub_tarea2 = Task("Sub-Subtarea 2")  # Crea otra sub sub tarea con el nombre "Sub-Subtarea 2"

    sub_tarea1.add_subtask(sub_sub_tarea1)  # Agrega la sub sub tarea 1 a la lista de sub tareas de la sub tarea 1
    sub_tarea1.add_subtask(sub_sub_tarea2)  # Agrega la sub sub tarea 2 a la lista de sub tareas de la sub tarea 1

    tarea_principal.add_subtask(sub_tarea1)  # Agrega la sub tarea 1 a la lista de sub tareas de la tarea principal
    tarea_principal.add_subtask(sub_tarea2)  # Agrega la sub tarea 2 a la lista de sub tareas de la tarea principal

    execute_task(tarea_principal)  # Ejecuta la tarea principal y todas sus sub tareas recursivamente
