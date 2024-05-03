##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la librería NumPy para manejar matrices y operaciones matemáticas

class ClasificadorBayesiano:
    def __init__(self):
        self.probabilidades_clase = {}  # Diccionario para almacenar las probabilidades de cada clase
        self.probabilidades_condicionales = {}  # Diccionario para almacenar las probabilidades condicionales de las características

    def entrenar(self, X, y):
        # Calcula la probabilidad de cada clase
        clases, counts = np.unique(y, return_counts=True)  # Obtiene las clases únicas y sus conteos en el conjunto de etiquetas y
        total = len(y)  # Calcula el total de etiquetas en y
        for i, clase in enumerate(clases):
            self.probabilidades_clase[clase] = counts[i] / total  # Calcula la probabilidad de cada clase

        # Calcula las probabilidades condicionales
        for clase in self.probabilidades_clase:
            indices_clase = np.where(y == clase)[0]  # Obtiene los índices de las instancias de la clase actual
            X_clase = X[indices_clase]  # Obtiene las características correspondientes a la clase actual
            media = np.mean(X_clase, axis=0)  # Calcula la media de las características para la clase actual
            varianza = np.var(X_clase, axis=0)  # Calcula la varianza de las características para la clase actual
            self.probabilidades_condicionales[clase] = (media, varianza)  # Almacena las medias y varianzas en el diccionario

    def predecir(self, X):
        predicciones = []  # Lista para almacenar las predicciones
        for x in X:  # Itera sobre cada instancia en X
            probabilidades = []  # Lista para almacenar las probabilidades de cada clase para la instancia actual
            for clase in self.probabilidades_clase:  # Itera sobre cada clase
                prob_clase = self.probabilidades_clase[clase]  # Obtiene la probabilidad de la clase actual
                media, varianza = self.probabilidades_condicionales[clase]  # Obtiene la media y varianza de la clase actual
                # Calcula la probabilidad usando la distribución normal
                prob = prob_clase * np.prod(1 / np.sqrt(2 * np.pi * varianza) * np.exp(-(x - media)**2 / (2 * varianza)))
                probabilidades.append(prob)  # Agrega la probabilidad a la lista
            predicciones.append(np.argmax(probabilidades))  # Agrega la clase con la probabilidad más alta como predicción
        return predicciones

# Ejemplo de uso
X = np.array([[1, 1], [2, 2], [3, 3], [6, 6], [7, 7], [8, 8]])  # Datos de entrada (características)
y = np.array([0, 0, 0, 1, 1, 1])  # Etiquetas de las clases correspondientes a los datos

clasificador = ClasificadorBayesiano()  # Crea una instancia del clasificador
clasificador.entrenar(X, y)  # Entrena el clasificador con los datos de entrenamiento

nuevos_datos = np.array([[4, 4], [5, 5]])  # Nuevos datos a predecir
predicciones = clasificador.predecir(nuevos_datos)  # Realiza predicciones para los nuevos datos
print("Predicciones:", predicciones)  # Imprime las predicciones
