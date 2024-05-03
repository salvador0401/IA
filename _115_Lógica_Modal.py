##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de la clase Mundo que representa un mundo en la lógica modal
class Mundo:
    def __init__(self, nombre, accesible=None):
        # Constructor de la clase Mundo
        self.nombre = nombre  # Nombre del mundo
        self.accesible = accesible if accesible else []  # Lista de mundos accesibles desde este mundo

    def agregar_accesible(self, mundo):
        # Método para agregar un mundo accesible desde este mundo
        self.accesible.append(mundo)

# Definición de la clase Agente que representa un agente en la lógica modal
class Agente:
    def __init__(self, nombre, mundo_actual):
        # Constructor de la clase Agente
        self.nombre = nombre  # Nombre del agente
        self.mundo_actual = mundo_actual  # Mundo en el que se encuentra el agente

    def ir_a_mundo(self, mundo):
        # Método para que el agente se mueva a otro mundo
        if mundo in self.mundo_actual.accesible:
            # Verifica si el mundo al que el agente quiere ir es accesible desde el mundo actual
            self.mundo_actual = mundo  # El agente se mueve al nuevo mundo
            print(f"{self.nombre} se mueve al mundo {mundo.nombre}")  # Mensaje de movimiento exitoso
        else:
            print(f"¡Error! {self.nombre} no puede ir al mundo {mundo.nombre}")
            # Mensaje de error si el mundo al que el agente quiere ir no es accesible desde el mundo actual

# Definición de mundos
mundo1 = Mundo("Mundo 1")  # Creamos el Mundo 1
mundo2 = Mundo("Mundo 2")  # Creamos el Mundo 2
mundo3 = Mundo("Mundo 3")  # Creamos el Mundo 3

# Conexiones entre mundos
mundo1.agregar_accesible(mundo2)  # Hacemos el Mundo 2 accesible desde el Mundo 1
mundo2.agregar_accesible(mundo3)  # Hacemos el Mundo 3 accesible desde el Mundo 2
mundo3.agregar_accesible(mundo1)  # Hacemos el Mundo 1 accesible desde el Mundo 3, creando un ciclo

# Crear un agente
agente1 = Agente("Agente 1", mundo1)  # Creamos el Agente 1 en el Mundo 1

# Ejemplo de movimiento del agente
agente1.ir_a_mundo(mundo2)  # El agente se mueve al Mundo 2
agente1.ir_a_mundo(mundo3)  # El agente se mueve al Mundo 3
agente1.ir_a_mundo(mundo1)  # El agente no puede ir al Mundo 1 desde Mundo 3, ya que Mundo 1 no es accesible desde Mundo 3
