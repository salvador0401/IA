##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class MejorHipotesisActual:
    def __init__(self, features, target):
        # Inicialización de la clase con características y variable objetivo
        self.features = features  # Lista de características
        self.target = target      # Nombre de la variable objetivo
        self.hypothesis = None    # Hipótesis inicialmente vacía

    def train(self, instances):
        # Método para entrenar el modelo
        self.hypothesis = {}  # Diccionario para almacenar la hipótesis
        for i, val in enumerate(self.features):
            # Encuentra el valor más frecuente para cada característica
            self.hypothesis[val] = self.find_most_frequent_value(instances, i)

    def find_most_frequent_value(self, instances, index):
        # Encuentra el valor más frecuente en una columna específica
        values = [instance[index] for instance in instances]
        return max(set(values), key=values.count)

    def predict(self, instance):
        # Método para predecir la clase de una nueva instancia
        if self.hypothesis is None:
            raise Exception("Model has not been trained yet.")
        prediction = self.hypothesis[self.features[0]]  # Predicción inicial
        for i, val in enumerate(self.features):
            # Compara cada característica de la instancia con la hipótesis
            if instance[i] != self.hypothesis[val]:
                return prediction  # Retorna la predicción actual
        return prediction  # Retorna la predicción final


# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo (características discretas)
    features = ['F1', 'F2', 'F3']  # Lista de características
    target = 'Clase'               # Variable objetivo
    instances = [                  # Instancias de entrenamiento
        ['A', 'X', 'Y', 'Positivo'],
        ['B', 'X', 'Y', 'Positivo'],
        ['A', 'Z', 'Y', 'Negativo'],
        ['B', 'Z', 'X', 'Negativo'],
        ['A', 'X', 'X', 'Positivo']
    ]

    # Entrenamiento del modelo
    mha = MejorHipotesisActual(features, target)
    mha.train(instances)

    # Predicción de nuevas instancias
    new_instance = ['B', 'X', 'X']   # Nueva instancia
    prediction = mha.predict(new_instance)  # Predicción
    print("Predicción:", prediction)  # Imprime la predicción
