##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Agente:
    def __init__(self, nombre):
        self.nombre = nombre # Asigna el nombre del agente
        self.tareas = [] # Inicializa una lista vacía para almacenar las tareas del agente

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea) # Agrega una tarea a la lista de tareas del agente

    def imprimir_tareas(self):
        print(f"Tareas del agente {self.nombre}:") # Imprime el encabezado con el nombre del agente
        for i, tarea in enumerate(self.tareas, 1): # Itera sobre las tareas del agente
            print(f"{i}. {tarea}") # Imprime el índice y el nombre de cada tarea

class Entorno:
    def __init__(self, agentes):
        self.agentes = agentes # Inicializa la lista de agentes en el entorno

    def asignar_tarea(self, agente, tarea):
        if agente in self.agentes: # Verifica si el agente está presente en el entorno
            agente.agregar_tarea(tarea) # Asigna la tarea al agente
            print(f"La tarea '{tarea}' ha sido asignada al agente '{agente.nombre}'.") # Imprime un mensaje de confirmación
        else:
            print(f"Error: El agente '{agente.nombre}' no existe en este entorno.") # Imprime un mensaje de error si el agente no está presente

def main():
    agente1 = Agente("Agente 1") # Crea un agente con nombre "Agente 1"
    agente2 = Agente("Agente 2") # Crea un agente con nombre "Agente 2"
    agente3 = Agente("Agente 3") # Crea un agente con nombre "Agente 3"

    entorno = Entorno([agente1, agente2, agente3]) # Crea un entorno con los agentes especificados

    # Se asignan tareas a los agentes
    entorno.asignar_tarea(agente1, "Reunión de equipo") # Asigna una tarea al agente 1
    entorno.asignar_tarea(agente2, "Preparación de informe") # Asigna una tarea al agente 2
    entorno.asignar_tarea(agente3, "Investigación de mercado") # Asigna una tarea al agente 3

    # Se imprimen las tareas asignadas a cada agente
    agente1.imprimir_tareas() # Imprime las tareas del agente 1
    agente2.imprimir_tareas() # Imprime las tareas del agente 2
    agente3.imprimir_tareas() # Imprime las tareas del agente 3

if __name__ == "__main__":
    main() # Llama a la función main si este script es ejecutado directamente
