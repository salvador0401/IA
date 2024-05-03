##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Genera datos de ejemplo con dos clusters
X, _ = make_blobs(n_samples=1000, centers=2, cluster_std=1.5, random_state=42)
# La función make_blobs genera datos de puntos con clusters. 

# Inicializa el modelo de mezcla de Gaussianas con dos componentes
modelo_em = GaussianMixture(n_components=2, random_state=42)
# Crea una instancia del modelo de mezcla de Gaussianas con 2 componentes.
# GaussianMixture es el estimador de scikit-learn que implementa el algoritmo EM para mezcla de Gaussianas.

# Entrena el modelo utilizando el algoritmo EM
modelo_em.fit(X)
# Entrena el modelo de mezcla de Gaussianas utilizando los datos X.

# Obtiene las etiquetas de cluster asignadas a cada muestra
etiquetas = modelo_em.predict(X)
# Predice el cluster al que pertenece cada muestra en X.

# Obtiene las medias y matrices de covarianza de los clusters
medias = modelo_em.means_
covarianzas = modelo_em.covariances_
# Obtiene las medias y matrices de covarianza de los clusters identificados por el modelo.

print("Medias de los clusters:")
print(medias)
print("\nMatrices de covarianza de los clusters:")
print(covarianzas)
# Imprime las medias y matrices de covarianza de los clusters identificados por el modelo.
