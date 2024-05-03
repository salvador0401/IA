##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Taxonomy:
    def __init__(self):
        # Inicializa la taxonomía como un diccionario vacío
        self.categories = {}

    def add_category(self, category, parent=None):
        # Agrega una categoría al diccionario de la taxonomía
        if category not in self.categories:
            self.categories[category] = set()  # Si la categoría no existe, crea un conjunto vacío para sus subcategorías
        if parent:  # Si se proporciona un padre, añade este a la lista de subcategorías
            if parent not in self.categories:
                self.categories[parent] = set()  # Si el padre no existe, crea un conjunto vacío para sus subcategorías
            self.categories[parent].add(category)  # Agrega la categoría como subcategoría del padre

    def get_subcategories(self, category):
        # Obtiene las subcategorías de una categoría dada
        if category in self.categories:
            return self.categories[category]  # Devuelve el conjunto de subcategorías
        else:
            return set()  # Devuelve un conjunto vacío si la categoría no tiene subcategorías

# Crear una instancia de la taxonomía
taxonomy = Taxonomy()

# Agregar categorías y subcategorías
taxonomy.add_category("Animal")
taxonomy.add_category("Mamífero", parent="Animal")
taxonomy.add_category("Reptil", parent="Animal")
taxonomy.add_category("Perro", parent="Mamífero")
taxonomy.add_category("Gato", parent="Mamífero")
taxonomy.add_category("Lagarto", parent="Reptil")

# Consultar subcategorías
print("Subcategorías de Animal:", taxonomy.get_subcategories("Animal"))
print("Subcategorías de Mamífero:", taxonomy.get_subcategories("Mamífero"))
print("Subcategorías de Reptil:", taxonomy.get_subcategories("Reptil"))

