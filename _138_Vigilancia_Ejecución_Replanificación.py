##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Tarea:
    def __init__(self, nombre, duracion): # Definición de la clase Tarea con un constructor que recibe el nombre y la duración de la tarea
        self.nombre = nombre # Asigna el nombre de la tarea al atributo 'nombre'
        self.duracion = duracion # Asigna la duración de la tarea al atributo 'duracion'

class Agenda:
    def __init__(self): # Definición de la clase Agenda con un constructor que inicializa la lista de tareas
        self.tareas = [] # Inicializa una lista vacía para almacenar las tareas

    def agregar_tarea(self, tarea): # Método para agregar una tarea a la agenda
        self.tareas.append(tarea) # Agrega la tarea a la lista de tareas

    def imprimir_agenda(self): # Método para imprimir la agenda actual
        print("Agenda:") # Imprime un encabezado
        for i, tarea in enumerate(self.tareas, 1): # Itera sobre todas las tareas en la lista
            print(f"{i}. {tarea.nombre} - Duración: {tarea.duracion} horas") # Imprime el nombre y la duración de cada tarea

class Planificador:
    def __init__(self): # Definición de la clase Planificador con un constructor que inicializa una instancia de Agenda
        self.agenda = Agenda() # Inicializa una instancia de Agenda

    def agregar_tarea(self, nombre, duracion): # Método para agregar una tarea a la agenda
        tarea = Tarea(nombre, duracion) # Crea una nueva instancia de Tarea con el nombre y la duración proporcionados
        self.agenda.agregar_tarea(tarea) # Agrega la tarea a la agenda

    def replanificar(self, tarea, nueva_duracion): # Método para replanificar una tarea existente
        for t in self.agenda.tareas: # Itera sobre todas las tareas en la agenda
            if t.nombre == tarea: # Si encuentra la tarea que se va a replanificar
                t.duracion = nueva_duracion # Actualiza la duración de la tarea
                print(f"La tarea '{tarea}' ha sido replanificada a {nueva_duracion} horas.") # Imprime un mensaje indicando que la tarea ha sido replanificada

def main():
    planificador = Planificador() # Crea una instancia de Planificador

    # Se agregan tareas a la agenda
    planificador.agregar_tarea("Reunión de equipo", 2) # Agrega una tarea a la agenda
    planificador.agregar_tarea("Preparación de informe", 3) # Agrega otra tarea a la agenda
    planificador.agregar_tarea("Investigación de mercado", 4) # Agrega otra tarea a la agenda

    # Se imprime la agenda actual
    planificador.agenda.imprimir_agenda() # Imprime la agenda actual

    # Se replanifica una tarea
    planificador.replanificar("Preparación de informe", 5) # Replanifica una tarea existente con una nueva duración

    # Se imprime la agenda actualizada
    planificador.agenda.imprimir_agenda() # Imprime la agenda actualizada

if __name__ == "__main__":
    main() # Llama a la función main si este script es ejecutado directamente
