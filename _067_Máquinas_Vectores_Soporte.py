##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la biblioteca numpy y la renombra como np
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib.pyplot y la renombra como plt
from sklearn.datasets import make_circles  # Importa la función make_circles del módulo datasets de la biblioteca sklearn
from sklearn.svm import SVC  # Importa la clase SVC (Support Vector Classifier) del módulo svm de la biblioteca sklearn

# Genera datos de ejemplo en forma de círculos con ruido y un factor de separación entre clases
X, y = make_circles(n_samples=100, noise=0.1, factor=0.5, random_state=42)

# Visualiza los datos de entrada
plt.figure(figsize=(6, 6))  # Crea una nueva figura con tamaño 6x6 pulgadas
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')  # Grafica los puntos de datos con colores basados en las etiquetas y
plt.title("Datos de entrada")  # Establece el título del gráfico como "Datos de entrada"
plt.xlabel("Característica 1")  # Etiqueta el eje x como "Característica 1"
plt.ylabel("Característica 2")  # Etiqueta el eje y como "Característica 2"
plt.show()  # Muestra el gráfico

# Entrena un modelo SVM con un kernel RBF (Radial Basis Function)
svm = SVC(kernel='rbf', C=1, gamma='scale', random_state=42)  # Crea una instancia del clasificador SVM con kernel RBF y otros parámetros
svm.fit(X, y)  # Entrena el modelo SVM con los datos de entrada X y las etiquetas y

# Función para visualizar las fronteras de decisión
def plot_decision_boundaries(model, X, y):
    h = .02  # Define el tamaño del paso para la malla
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1  # Calcula los límites del eje x
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1  # Calcula los límites del eje y
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))  # Crea una malla de puntos para la visualización
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])  # Realiza predicciones para cada punto de la malla
    Z = Z.reshape(xx.shape)  # Ajusta la forma de Z para que coincida con la malla
    plt.contourf(xx, yy, Z, alpha=0.8, cmap='viridis')  # Grafica las regiones de decisión
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')  # Grafica los puntos de datos
# Visualiza las fronteras de decisión del modelo SVM
plt.figure(figsize=(6, 6))  # Crea una nueva figura con tamaño 6x6 pulgadas
plot_decision_boundaries(svm, X, y)  # Llama a la función plot_decision_boundaries para visualizar las fronteras de decisión
plt.title("Fronteras de decisión SVM con kernel RBF")  # Establece el título del gráfico como "Fronteras de decisión SVM con kernel RBF"
plt.xlabel("Característica 1")  # Etiqueta el eje x como "Característica 1"
plt.ylabel("Característica 2")  # Etiqueta el eje y como "Característica 2"
plt.show()  # Muestra el gráfico
