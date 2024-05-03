##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de la clase Regla
class Regla:
    def __init__(self, condiciones, clase):
        # Inicializa la regla con las condiciones y la clase asociada
        self.condiciones = condiciones  # Condiciones de la regla
        self.clase = clase  # Clase asociada a la regla

    def cubre(self, instancia):
        # Verifica si la regla cubre la instancia
        for i, condicion in enumerate(self.condiciones):
            # Compara cada condición de la regla con la instancia actual
            if condicion != instancia[i] and condicion != '?':
                # Si la condición no coincide con la instancia y no es un valor de "don't care" ('?'), la regla no cubre la instancia
                return False
        # Si todas las condiciones coinciden (o son "don't care"), la regla cubre la instancia
        return True

# Definición de la clase AprendizajeInductivo
class AprendizajeInductivo:
    def __init__(self, features, target):
        # Inicializa el AprendizajeInductivo con las características y la variable objetivo
        self.features = features  # Características
        self.target = target  # Variable objetivo
        self.reglas = []  # Lista de reglas

    def train(self, instances):
        # Entrena el modelo generando reglas para cada instancia
        for instance in instances:
            # Crea una regla con las características de la instancia y la clase asociada
            regla = Regla(instance[:-1], instance[-1])
            # Agrega la regla a la lista de reglas
            self.reglas.append(regla)

    def explain(self, instance):
        # Explica la predicción para una instancia dada utilizando las reglas generadas
        explanations = []
        for regla in self.reglas:
            if regla.cubre(instance):
                # Si una regla cubre la instancia, agrega la regla y su clase asociada a las explicaciones
                explanation = {
                    'regla': regla.condiciones,
                    'clase': regla.clase
                }
                explanations.append(explanation)
        return explanations

# Datos de ejemplo
instances = [
    ['Nublado', 'Frio', 'Alto', 'No'],
    ['Soleado', 'Calor', 'Normal', 'Si'],
    ['Nublado', 'Calor', 'Alto', 'Si'],
    ['Lluvia', 'Frio', 'Normal', 'No'],
    ['Soleado', 'Templado', 'Alto', 'Si']
]

# Entrenamiento del modelo
ai = AprendizajeInductivo(features=['Tiempo', 'Temperatura', 'Humedad'], target='Jugar')
ai.train(instances)

# Explicaciones e información relevante para nuevas instancias
new_instance = ['Soleado', 'Frio', 'Alto']
explanations = ai.explain(new_instance)
print("Explicaciones para la instancia", new_instance)
for explanation in explanations:
    print("Regla:", explanation['regla'], "Clase:", explanation['clase'])
