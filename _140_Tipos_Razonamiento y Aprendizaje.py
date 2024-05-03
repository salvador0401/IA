##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Animal:  # Define una clase llamada Animal
    def __init__(self, nombre, tipo, pelo, patas):  # Define el método de inicialización de la clase Animal con atributos nombre, tipo, pelo y patas
        self.nombre = nombre  # Asigna el nombre del animal
        self.tipo = tipo  # Asigna el tipo del animal (por ejemplo, mamífero, ave, reptil)
        self.pelo = pelo  # Indica si el animal tiene pelo (True o False)
        self.patas = patas  # Indica el número de patas del animal

# Datos de entrenamiento
animales_entrenamiento = [  # Lista de objetos de la clase Animal que representan animales con atributos específicos
    Animal("Perro", "mamífero", True, 4),  # Ejemplo de un perro, un mamífero con pelo y cuatro patas
    Animal("Gato", "mamífero", True, 4),  # Ejemplo de un gato, un mamífero con pelo y cuatro patas
    Animal("Pato", "ave", False, 2),  # Ejemplo de un pato, un ave sin pelo y con dos patas
    Animal("Ballena", "mamífero", False, 0),  # Ejemplo de una ballena, un mamífero sin pelo y sin patas (nadador)
    Animal("Cebra", "mamífero", True, 4),  # Ejemplo de una cebra, un mamífero con pelo y cuatro patas
    Animal("Tortuga", "reptil", False, 4)  # Ejemplo de una tortuga, un reptil sin pelo y con cuatro patas
]

# Función para determinar si un animal es un mamífero basado en características
def es_mamifero(animal):  # Define una función que toma un objeto Animal y devuelve True si es mamífero, False en caso contrario
    return animal.pelo and animal.patas == 4  # Retorna True si el animal tiene pelo y cuatro patas, False en caso contrario

# Algoritmo de aprendizaje inductivo
def aprendizaje_inductivo(animales):  # Define una función que toma una lista de animales y retorna una lista de mamíferos identificados
    mamiferos_identificados = []  # Inicializa una lista vacía para almacenar los mamíferos identificados
    for animal in animales:  # Itera sobre cada animal en la lista de animales
        if es_mamifero(animal):  # Verifica si el animal es un mamífero usando la función es_mamifero
            mamiferos_identificados.append(animal.nombre)  # Agrega el nombre del animal a la lista de mamíferos identificados
    return mamiferos_identificados  # Retorna la lista de mamíferos identificados

# Función para mostrar resultados
def mostrar_resultados(mamiferos_identificados):  # Define una función que muestra los mamíferos identificados
    if len(mamiferos_identificados) > 0:  # Verifica si se identificaron mamíferos
        print("Los siguientes animales son identificados como mamíferos:")  # Imprime un mensaje indicando que se identificaron mamíferos
        for animal in mamiferos_identificados:  # Itera sobre cada mamífero identificado
            print("- " + animal)  # Imprime el nombre del mamífero
    else:  # Si no se identificaron mamíferos
        print("No se identificaron mamíferos en el conjunto de datos de entrada.")  # Imprime un mensaje indicando que no se identificaron mamíferos

# Ejecución del programa
mamiferos_identificados = aprendizaje_inductivo(animales_entrenamiento)  # Llama a la función aprendizaje_inductivo con los datos de entrenamiento
mostrar_resultados(mamiferos_identificados)  # Muestra los resultados del aprendizaje inductivo
