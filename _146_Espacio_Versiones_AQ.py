##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class EspacioVersiones:
    def __init__(self, num_features):
        # Inicializa el objeto EspacioVersiones con el número de características especificado
        self.num_features = num_features
        # Inicializa la hipótesis con una lista de longitud num_features, con todos los elementos como '0'
        self.hypothesis = ['0'] * num_features

    def generalize(self, instance):
        # Generaliza la hipótesis basada en una instancia dada
        for i, value in enumerate(instance):
            if self.hypothesis[i] != value:
                self.hypothesis[i] = '?'

    def specialize(self, instance):
        # Especializa la hipótesis basada en una instancia dada
        for i, value in enumerate(instance):
            if self.hypothesis[i] == '?':
                self.hypothesis[i] = value

    def predict(self, instance):
        # Predice la clase de una instancia dada utilizando la hipótesis actual
        for i, value in enumerate(instance):
            if self.hypothesis[i] != '?' and self.hypothesis[i] != value:
                return 'No se puede clasificar'
        return 'Positivo'

class AQ:
    def __init__(self, num_features):
        # Inicializa el objeto AQ con una hipótesis inicial creada utilizando EspacioVersiones
        self.hypothesis = EspacioVersiones(num_features)

    def train(self, instances):
        # Entrena el modelo AQ utilizando instancias etiquetadas
        for instance in instances:
            if instance[-1] == 'Positivo':
                # Generaliza si la etiqueta es 'Positivo'
                self.hypothesis.generalize(instance[:-1])
            else:
                # Especializa si la etiqueta es 'Negativo'
                self.hypothesis.specialize(instance[:-1])

    def predict(self, instance):
        # Predice la clase de una instancia dada utilizando la hipótesis aprendida
        return self.hypothesis.predict(instance)

# Datos de ejemplo
instances = [
    ['1', '1', 'Positivo'],
    ['0', '0', 'Negativo'],
    ['0', '1', 'Negativo'],
    ['1', '0', 'Positivo']
]

# Entrenamiento del modelo
aq = AQ(num_features=2)
aq.train(instances)

# Predicción de nuevas instancias
new_instances = [
    ['1', '1'],
    ['0', '1'],
    ['1', '0'],
    ['0', '0']
]

for instance in new_instances:
    # Realiza predicciones para cada nueva instancia y muestra el resultado
    prediction = aq.predict(instance)
    print("Instancia:", instance, "Predicción:", prediction)
