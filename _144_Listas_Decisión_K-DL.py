##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Importar la biblioteca NumPy y la renombramos como np
import numpy as np

class KDLClassifier:
    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        # Almacenar los datos de entrenamiento
        self.X = X
        self.y = y

    def predict(self, X):
        # Inicializar una lista para almacenar las predicciones
        y_pred = []
        # Iterar sobre cada muestra en el conjunto de datos de prueba
        for sample in X:
            # Calcular las distancias euclidianas entre la muestra actual y todas las muestras de entrenamiento
            distances = np.sqrt(np.sum((self.X - sample) ** 2, axis=1))
            # Encontrar los índices de las k muestras más cercanas
            k_nearest_indices = np.argsort(distances)[:self.k]
            # Obtener las etiquetas correspondientes a las k muestras más cercanas
            k_nearest_labels = self.y[k_nearest_indices]
            # Contar las ocurrencias de cada etiqueta
            unique_labels, counts = np.unique(k_nearest_labels, return_counts=True)
            # Predecir la etiqueta más frecuente como la etiqueta de la muestra actual
            predicted_label = unique_labels[np.argmax(counts)]
            # Agregar la etiqueta predicha a la lista de predicciones
            y_pred.append(predicted_label)
        # Convertir la lista de predicciones en un array NumPy y devolverlo
        return np.array(y_pred)

# Ejemplo de uso
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el clasificador K-DL
kdl_classifier = KDLClassifier(k=5)
kdl_classifier.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = kdl_classifier.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador K-DL:", accuracy)

