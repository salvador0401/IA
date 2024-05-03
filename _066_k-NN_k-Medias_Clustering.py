##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.neighbors import KNeighborsClassifier

# Genera datos de ejemplo con tres clusters
X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.6, random_state=42)
# Utilizamos la función make_blobs para generar datos de ejemplo.
# Especificamos que queremos 300 puntos distribuidos en 3 clusters,
# con una desviación estándar de 0.6 y una semilla aleatoria fija para reproducibilidad.

# Visualiza los datos de entrada
plt.figure(figsize=(12, 4))
# Creamos una nueva figura para mostrar los gráficos.

plt.subplot(131)
# Creamos un subplot en la primera posición (1 fila, 3 columnas, posición 1).
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
# Dibujamos los puntos de datos, coloreándolos según sus etiquetas de clase (y).
plt.title("Datos de entrada")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
# Agregamos título y etiquetas de ejes.

# Aplica k-NN
knn = KNeighborsClassifier(n_neighbors=3)
# Creamos una instancia del clasificador k-NN con k=3.
knn.fit(X, y)
# Entrenamos el clasificador k-NN con los datos de entrada.

# Visualiza el resultado de k-NN
plt.subplot(132)
# Creamos un subplot en la segunda posición (1 fila, 3 columnas, posición 2).
plt.scatter(X[:, 0], X[:, 1], c=knn.predict(X), cmap='viridis')
# Dibujamos los puntos de datos, coloreándolos según las predicciones del clasificador k-NN.
plt.title("k-NN")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
# Agregamos título y etiquetas de ejes.

# Aplica k-Means
kmeans = KMeans(n_clusters=3, random_state=42)
# Creamos una instancia del algoritmo k-Means con 3 clusters y una semilla aleatoria fija.
kmeans.fit(X)
# Aplicamos el algoritmo k-Means a los datos de entrada.

# Visualiza el resultado de k-Means
plt.subplot(133)
# Creamos un subplot en la tercera posición (1 fila, 3 columnas, posición 3).
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
# Dibujamos los puntos de datos, coloreándolos según las etiquetas de cluster asignadas por k-Means.
plt.title("k-Means")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
# Agregamos título y etiquetas de ejes.

plt.tight_layout()
# Ajustamos el diseño para evitar superposiciones.
plt.show()
# Mostramos la figura con los gráficos.
