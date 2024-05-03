##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Importar las bibliotecas necesarias
from sklearn.datasets import load_iris  # Importar la función load_iris desde sklearn.datasets
from sklearn.model_selection import train_test_split  # Importar la función train_test_split desde sklearn.model_selection
from sklearn.tree import DecisionTreeClassifier  # Importar la clase DecisionTreeClassifier desde sklearn.tree
from sklearn.metrics import accuracy_score  # Importar la función accuracy_score desde sklearn.metrics

# Cargar el conjunto de datos Iris
iris = load_iris()  # Cargar el conjunto de datos Iris
X = iris.data  # Obtener las características de los datos
y = iris.target  # Obtener las etiquetas de los datos

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Dividir los datos en conjuntos de entrenamiento y prueba

# Crear un clasificador de árbol de decisión K-DT
k_dt_classifier = DecisionTreeClassifier()  # Crear un clasificador de árbol de decisión

# Entrenar el clasificador
k_dt_classifier.fit(X_train, y_train)  # Entrenar el clasificador con los datos de entrenamiento

# Realizar predicciones en el conjunto de prueba
y_pred = k_dt_classifier.predict(X_test)  # Realizar predicciones sobre los datos de prueba

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)  # Calcular la precisión comparando las etiquetas verdaderas con las predichas
print("Precisión del clasificador K-DT:", accuracy)  # Imprimir la precisión obtenida
