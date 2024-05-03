##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from sklearn.datasets import load_iris  # Importa la función para cargar el conjunto de datos Iris
from sklearn.model_selection import train_test_split  # Importa la función para dividir el conjunto de datos en entrenamiento y prueba
from sklearn.naive_bayes import GaussianNB  # Importa el clasificador Naïve Bayes Gaussiano
from sklearn.metrics import accuracy_score  # Importa la función para calcular la precisión del modelo

# Cargar el conjunto de datos Iris
iris = load_iris()  # Carga el conjunto de datos Iris

X = iris.data  # Características (longitud y ancho del sépalo y del pétalo)
y = iris.target  # Etiquetas (especies de iris)

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Divide aleatoriamente el conjunto de datos en conjuntos de entrenamiento y prueba,
# reservando el 20% de los datos para pruebas y utilizando una semilla aleatoria para reproducibilidad

# Crear un clasificador Naïve Bayes Gaussiano
naive_bayes = GaussianNB()  # Crea una instancia del clasificador Naïve Bayes Gaussiano

# Entrenar el clasificador
naive_bayes.fit(X_train, y_train)  # Entrena el clasificador con los datos de entrenamiento

# Realizar predicciones en el conjunto de prueba
predicciones = naive_bayes.predict(X_test)  # Realiza predicciones utilizando el conjunto de prueba

# Calcular la precisión
precision = accuracy_score(y_test, predicciones)  # Calcula la precisión comparando las etiquetas verdaderas con las predicciones
print("Precisión:", precision)  # Imprime la precisión del modelo
