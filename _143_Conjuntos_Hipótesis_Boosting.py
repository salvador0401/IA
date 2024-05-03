##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importamos la biblioteca NumPy y la renombramos como np
from sklearn.datasets import load_iris  # Importamos la función load_iris desde sklearn.datasets
from sklearn.model_selection import train_test_split  # Importamos la función train_test_split desde sklearn.model_selection
from sklearn.ensemble import AdaBoostClassifier  # Importamos la clase AdaBoostClassifier desde sklearn.ensemble
from sklearn.metrics import accuracy_score  # Importamos la función accuracy_score desde sklearn.metrics

# Cargamos el conjunto de datos Iris
iris = load_iris()  # Cargamos el conjunto de datos Iris
X = iris.data  # Obtenemos las características de los datos
y = iris.target  # Obtenemos las etiquetas de los datos

# Dividimos el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Dividimos los datos en conjuntos de entrenamiento y prueba

# Creamos el clasificador AdaBoost
n_estimators = 50  # Número de clasificadores débiles en el conjunto
learning_rate = 1.0  # Tasa de aprendizaje
boosting_classifier = AdaBoostClassifier(n_estimators=n_estimators,  # Creamos un clasificador AdaBoost con el número de estimadores especificado
                                         learning_rate=learning_rate,  # Asignamos la tasa de aprendizaje especificada
                                         random_state=42)  # Fijamos la semilla aleatoria para reproducibilidad

# Entrenamos el clasificador
boosting_classifier.fit(X_train, y_train)  # Entrenamos el clasificador AdaBoost utilizando los datos de entrenamiento

# Realizamos predicciones en el conjunto de prueba
y_pred = boosting_classifier.predict(X_test)  # Realizamos predicciones sobre los datos de prueba

# Calculamos la precisión
accuracy = accuracy_score(y_test, y_pred)  # Calculamos la precisión comparando las etiquetas verdaderas con las predichas
print("Precisión:", accuracy)  # Imprimimos la precisión obtenida
