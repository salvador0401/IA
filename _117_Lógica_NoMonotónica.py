##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de la clase BaseConocimiento que representa la base de conocimiento del agente
class BaseConocimiento:
    def __init__(self):
        # Constructor de la clase BaseConocimiento
        self.hechos = []  # Lista para almacenar los hechos conocidos

    def agregar_hecho(self, hecho):
        # Método para agregar un hecho a la base de conocimiento
        self.hechos.append(hecho)

    def consultar_hecho(self, hecho):
        # Método para consultar si un hecho está en la base de conocimiento
        return hecho in self.hechos

# Definición de la clase Agente que representa al agente
class Agente:
    def __init__(self, base_conocimiento):
        # Constructor de la clase Agente
        self.base_conocimiento = base_conocimiento  # La base de conocimiento asociada al agente

    def realizar_accion(self, accion):
        # Método para realizar una acción basada en el conocimiento del agente
        if self.base_conocimiento.consultar_hecho(accion):
            # Verifica si la acción está en la base de conocimiento
            print(f"Realizando la acción: {accion}")  # Mensaje de que se realiza la acción
        else:
            print(f"No se realiza la acción {accion} debido a la incertidumbre.")
            # Mensaje de que no se realiza la acción debido a la incertidumbre

# Crear una base de conocimiento
base_conocimiento = BaseConocimiento()

# Agregar hechos a la base de conocimiento
base_conocimiento.agregar_hecho("Accion1")
base_conocimiento.agregar_hecho("Accion2")

# Crear un agente con la base de conocimiento
agente = Agente(base_conocimiento)

# Realizar acciones
agente.realizar_accion("Accion1")  # El agente realiza Accion1
agente.realizar_accion("Accion3")  # El agente no realiza Accion3 debido a la incertidumbre
