##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Ontology:
    def __init__(self):
        # Inicializa la ontología como un diccionario vacío
        self.ontology = {}

    def add_relation(self, subject, relation, object):
        # Agrega una relación al diccionario de la ontología
        if subject not in self.ontology:
            self.ontology[subject] = {}  # Si el sujeto no está en la ontología, crea una entrada para él
        if relation not in self.ontology[subject]:
            self.ontology[subject][relation] = set()  # Si la relación no está en el sujeto, crea una entrada para ella
        self.ontology[subject][relation].add(object)  # Agrega el objeto a la relación

    def query(self, subject, relation):
        # Consulta la ontología para obtener información sobre una relación específica de un sujeto
        if subject in self.ontology and relation in self.ontology[subject]:
            return self.ontology[subject][relation]  # Devuelve el conjunto de objetos relacionados
        else:
            return set()  # Devuelve un conjunto vacío si no hay información sobre la relación

# Crear una instancia de la ontología
ontology = Ontology()

# Agregar relaciones a la ontología
ontology.add_relation("Perro", "es_un", "Animal")  # El perro es un animal
ontology.add_relation("Perro", "tiene", "Cuatro patas")  # Los perros tienen cuatro patas
ontology.add_relation("Perro", "hace", "Ladrar")  # Los perros ladran
ontology.add_relation("Perro", "come", "Carne")  # Los perros comen carne
ontology.add_relation("Gato", "es_un", "Animal")  # El gato es un animal
ontology.add_relation("Gato", "tiene", "Cuatro patas")  # Los gatos tienen cuatro patas
ontology.add_relation("Gato", "hace", "Maullar")  # Los gatos maúllan
ontology.add_relation("Gato", "come", "Pescado")  # Los gatos comen pescado

# Consultar la ontología
print("El perro es un:", ontology.query("Perro", "es_un"))  # Consulta si el perro es un animal
print("El gato tiene:", ontology.query("Gato", "tiene"))  # Consulta si el gato tiene cuatro patas
print("¿Qué hace un perro?", ontology.query("Perro", "hace"))  # Consulta qué hacen los perros
print("¿Qué hace un gato?", ontology.query("Gato", "hace"))  # Consulta qué hacen los gatos
print("¿Qué come un perro?", ontology.query("Perro", "come"))  # Consulta qué comen los perros
print("¿Qué come un gato?", ontology.query("Gato", "come"))  # Consulta qué comen los gatos

