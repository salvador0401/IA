##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Creencia:
    def __init__(self, sujeto, objeto, predicado):
        self.sujeto = sujeto  # El sujeto de la creencia, por ejemplo, una persona
        self.objeto = objeto  # El objeto de la creencia, por ejemplo, un objeto físico o mental
        self.predicado = predicado  # El predicado que relaciona el sujeto y el objeto

    def __str__(self):
        return f"({self.sujeto}, {self.predicado}, {self.objeto})"  # Representación en cadena de la creencia

class BaseConocimiento:
    def __init__(self):
        self.creencias = []  # Lista para almacenar las creencias

    def agregar_creencia(self, creencia):
        self.creencias.append(creencia)  # Agrega una nueva creencia a la lista

    def consultar_creencias(self):
        for creencia in self.creencias:
            print(creencia)  # Imprime cada creencia en la lista

# Crear una base de conocimiento
bc = BaseConocimiento()

# Agregar creencias a la base de conocimiento
bc.agregar_creencia(Creencia("Juan", "pizza", "gusta"))  # Juan gusta de la pizza
bc.agregar_creencia(Creencia("María", "guitarra", "toca"))  # María toca la guitarra
bc.agregar_creencia(Creencia("Ana", "libro", "lee"))  # Ana lee libros

# Consultar las creencias en la base de conocimiento
print("Creencias en la base de conocimiento:")
bc.consultar_creencias()
