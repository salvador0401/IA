##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de la clase MundoTemporal que representa un mundo en la lógica temporal
class MundoTemporal:
    def __init__(self, nombre, eventos=None):
        # Constructor de la clase MundoTemporal
        self.nombre = nombre  # Nombre del mundo temporal
        self.eventos = eventos if eventos else []  # Lista de eventos en este mundo temporal

    def agregar_evento(self, evento):
        # Método para agregar un evento al mundo temporal
        self.eventos.append(evento)

# Definición de la clase AgenteTemporal que representa un agente en la lógica temporal
class AgenteTemporal:
    def __init__(self, nombre, mundo_actual):
        # Constructor de la clase AgenteTemporal
        self.nombre = nombre  # Nombre del agente temporal
        self.mundo_actual = mundo_actual  # Mundo temporal en el que se encuentra el agente

    def ejecutar_evento(self, evento):
        # Método para que el agente temporal ejecute un evento
        if evento in self.mundo_actual.eventos:
            # Verifica si el evento está presente en el mundo temporal actual
            print(f"{self.nombre} ejecuta el evento {evento}")  # Mensaje de ejecución del evento
        else:
            print(f"¡Error! {self.nombre} no puede ejecutar el evento {evento}")
            # Mensaje de error si el evento no está presente en el mundo temporal actual

# Definición de mundos temporales
mundo_actual = MundoTemporal("Mundo Actual", ["evento1", "evento2"])  # Creamos el Mundo Actual con eventos
mundo_futuro = MundoTemporal("Mundo Futuro")  # Creamos el Mundo Futuro sin eventos

# Crear un agente temporal
agente_temporal = AgenteTemporal("Agente Temporal", mundo_actual)  # Creamos el Agente Temporal en el Mundo Actual

# Ejemplo de ejecución de eventos por el agente
agente_temporal.ejecutar_evento("evento1")  # El agente ejecuta el evento evento1
agente_temporal.ejecutar_evento("evento3")  # El agente no puede ejecutar el evento evento3 ya que no está en el mundo actual
