##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class FOIL:  # Definición de la clase FOIL
    def __init__(self, target_predicate, background_knowledge):  # Método constructor que recibe el predicado objetivo y el conocimiento de fondo
        self.target_predicate = target_predicate  # Predicado objetivo (clase)
        self.background_knowledge = background_knowledge  # Conocimiento de fondo

    def train(self, examples):  # Método para entrenar el modelo, recibe ejemplos de entrenamiento
        # Encuentra la cláusula más específica
        self.specific_clause = self.find_specific_clause(examples)

        # Encuentra la cláusula más general
        self.general_clause = self.find_general_clause(examples)

    def find_specific_clause(self, examples):  # Método para encontrar la cláusula más específica, recibe ejemplos de entrenamiento
        specific_clause = []  # Inicialización de la lista de la cláusula específica

        for example in examples:  # Itera sobre los ejemplos
            if example[1] == 'Yes':  # Si el ejemplo pertenece a la clase positiva
                specific_clause.append(example[0])  # Agrega las características a la cláusula específica

        return specific_clause  # Devuelve la cláusula específica

    def find_general_clause(self, examples):  # Método para encontrar la cláusula más general, recibe ejemplos de entrenamiento
        general_clause = []  # Inicialización de la lista de la cláusula general

        for example in examples:  # Itera sobre los ejemplos
            if example[1] == 'No':  # Si el ejemplo no pertenece a la clase positiva
                general_clause.append(example[0])  # Agrega las características a la cláusula general

        return general_clause  # Devuelve la cláusula general

    def predict(self, example):  # Método para predecir la clase de un ejemplo dado
        # Comprueba si el ejemplo satisface la cláusula específica
        for term in self.specific_clause:  # Itera sobre los términos de la cláusula específica
            if term not in example[0]:  # Si un término no está presente en el ejemplo
                return 'No'  # Devuelve 'No'

        # Comprueba si el ejemplo no satisface la cláusula general
        for term in self.general_clause:  # Itera sobre los términos de la cláusula general
            if term in example[0]:  # Si un término está presente en el ejemplo
                return 'No'  # Devuelve 'No'

        return 'Yes'  # Si no se cumple ninguna de las condiciones anteriores, devuelve 'Yes'

# Datos de ejemplo (Formato: (Características, Clase))
examples = [  # Definición de ejemplos de entrenamiento
    (['nublado', 'frío', 'normal'], 'No'),  # Ejemplo 1
    (['soleado', 'calor', 'alta'], 'Yes'),  # Ejemplo 2
    (['nublado', 'calor', 'normal'], 'Yes'),  # Ejemplo 3
    (['lluvia', 'frío', 'normal'], 'No'),  # Ejemplo 4
    (['soleado', 'templado', 'alta'], 'Yes')  # Ejemplo 5
]

# Definición del predicado objetivo y el conocimiento de fondo
target_predicate = 'Jugar'  # Predicado objetivo
background_knowledge = []  # Conocimiento de fondo (vacío en este caso)

# Entrenamiento del modelo FOIL
foil = FOIL(target_predicate, background_knowledge)  # Creación de una instancia de FOIL
foil.train(examples)  # Entrenamiento del modelo con los ejemplos

# Predicción para un nuevo ejemplo
new_example = (['soleado', 'frio', 'normal'], 'Unknown')  # Definición de un ejemplo desconocido
prediction = foil.predict(new_example)  # Predicción de la clase del nuevo ejemplo
print("Predicción para el ejemplo:", prediction)  # Impresión de la predicción
