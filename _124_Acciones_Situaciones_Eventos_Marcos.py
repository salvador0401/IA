##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Marco:
    def __init__(self, nombre, atributos=None): # Define la clase Marco con un constructor que recibe un nombre y atributos opcionales
        self.nombre = nombre # Asigna el nombre del marco
        self.atributos = atributos if atributos is not None else {} # Asigna los atributos del marco, si se proporcionan; de lo contrario, crea un diccionario vacío

    def agregar_atributo(self, clave, valor): # Método para agregar un atributo al marco
        self.atributos[clave] = valor # Asigna el valor al atributo especificado

    def __str__(self): # Método para representar el marco como una cadena
        return f"{self.nombre}: {self.atributos}" # Retorna una cadena que muestra el nombre del marco y sus atributos

class BaseConocimiento:
    def __init__(self): # Define la clase BaseConocimiento con un constructor
        self.marcos = {} # Inicializa un diccionario para almacenar los marcos

    def definir_marco(self, nombre, atributos=None): # Método para definir un nuevo marco en la base de conocimiento
        marco = Marco(nombre, atributos) # Crea un nuevo objeto Marco con el nombre y atributos dados
        self.marcos[nombre] = marco # Agrega el marco al diccionario de marcos, utilizando el nombre como clave

    def encontrar_marco(self, nombre): # Método para encontrar un marco por su nombre
        return self.marcos.get(nombre) # Retorna el marco correspondiente al nombre dado, si existe

    def agregar_atributo_a_marco(self, nombre_marco, clave, valor): # Método para agregar un atributo a un marco existente
        marco = self.encontrar_marco(nombre_marco) # Encuentra el marco con el nombre dado
        if marco: # Verifica si se encontró el marco
            marco.agregar_atributo(clave, valor) # Llama al método agregar_atributo del marco encontrado
        else:
            print(f"Error: Marco '{nombre_marco}' no encontrado.") # Imprime un mensaje de error si el marco no se encuentra

    def mostrar_marcos(self): # Método para mostrar todos los marcos en la base de conocimiento
        for nombre, marco in self.marcos.items(): # Itera sobre cada par clave-valor en el diccionario de marcos
            print(marco) # Imprime el marco

# Crear una base de conocimiento
bc = BaseConocimiento()

# Definir marcos para representar acciones, situaciones y eventos
bc.definir_marco("Accion", {"actor": "", "accion": "", "objeto": ""})
bc.definir_marco("Situacion", {"lugar": "", "participantes": [], "contexto": ""})
bc.definir_marco("Evento", {"situacion": "", "acciones": [], "tiempo": ""})

# Agregar instancias de marcos
bc.agregar_atributo_a_marco("Accion", "actor", "Juan")
bc.agregar_atributo_a_marco("Accion", "accion", "comió")
bc.agregar_atributo_a_marco("Accion", "objeto", "pizza")

bc.agregar_atributo_a_marco("Situacion", "lugar", "restaurante")
bc.agregar_atributo_a_marco("Situacion", "participantes", ["Juan", "María"])
bc.agregar_atributo_a_marco("Situacion", "contexto", "celebración de cumpleaños")

bc.agregar_atributo_a_marco("Evento", "situacion", "Situacion: {'lugar': 'restaurante', 'participantes': ['Juan', 'María'], 'contexto': 'celebración de cumpleaños'}")
bc.agregar_atributo_a_marco("Evento", "acciones", ["Accion: {'actor': 'Juan', 'accion': 'comió', 'objeto': 'pizza'}"])
bc.agregar_atributo_a_marco("Evento", "tiempo", "2024-04-02")

# Mostrar la base de conocimiento
bc.mostrar_marcos()
