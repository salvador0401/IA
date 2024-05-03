##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class KnowledgeBase:
    def __init__(self):
        self.beliefs = {}  # Diccionario para almacenar creencias (probabilidades) iniciales

    def add_belief(self, event, belief):
        self.beliefs[event] = belief  # Agrega una creencia (probabilidad) para un evento dado

    def get_belief(self, event):
        return self.beliefs.get(event, 0.0)  # Obtiene la creencia (probabilidad) para un evento dado, si no está presente, devuelve 0.0

    def update_belief(self, event, new_belief):
        if event in self.beliefs:
            self.beliefs[event] = new_belief  # Actualiza la creencia (probabilidad) para un evento dado si ya está presente
        else:
            print(f"El evento {event} no está en la base de conocimiento.")

    def print_beliefs(self):
        for event, belief in self.beliefs.items():
            print(f"{event}: {belief}")  # Imprime las creencias de todos los eventos en la base de conocimiento

# Creamos una base de conocimiento
kb = KnowledgeBase()

# Añadimos creencias iniciales
kb.add_belief("soleado", 0.6)  # Creencia inicial: hay un 60% de probabilidad de que sea soleado
kb.add_belief("nublado", 0.3)  # Creencia inicial: hay un 30% de probabilidad de que esté nublado
kb.add_belief("lluvioso", 0.1)  # Creencia inicial: hay un 10% de probabilidad de que llueva

# Mostramos las creencias iniciales
print("Creencias iniciales:")
kb.print_beliefs()
print()

# Actualizamos la creencia de un evento
kb.update_belief("soleado", 0.8)  # Actualizamos la creencia sobre el evento "soleado" a un 80%

# Mostramos las creencias actualizadas
print("Creencias actualizadas:")
kb.print_beliefs()
