##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class DefaultLogic:
    def __init__(self):
        self.knowledge_base = {}  # Base de conocimientos

    def add_rule(self, rule, conclusion):
        if conclusion not in self.knowledge_base:
            self.knowledge_base[conclusion] = []  # Si la conclusión no está en la base de conocimientos, crea una nueva lista vacía para almacenar las reglas asociadas a esa conclusión
        self.knowledge_base[conclusion].append(rule)  # Agrega la regla a la lista de reglas asociadas a la conclusión

    def infer(self, query):
        if query in self.knowledge_base:  # Si la consulta está en la base de conocimientos
            print("La conclusión es verdadera debido a las siguientes reglas:")
            for rule in self.knowledge_base[query]:  # Itera sobre todas las reglas asociadas a la consulta
                print("- ", rule)  # Imprime cada regla asociada a la consulta
        else:
            print("No se puede inferir la verdad de la conclusión.")  # Si la consulta no está en la base de conocimientos, imprime un mensaje indicando que no se puede inferir

# Crear una instancia de la lógica por defecto
dl = DefaultLogic()

# Agregar reglas a la base de conocimientos
dl.add_rule("Si es un ave, entonces vuela.", "vuela")
dl.add_rule("Si es un pingüino, entonces no vuela.", "no vuela")

# Consulta
query = "vuela"
dl.infer(query)  # Realiza una inferencia basada en la consulta y muestra el resultado
