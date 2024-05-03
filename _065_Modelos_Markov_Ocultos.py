##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np
from hmmlearn import hmm

# Definición del modelo HMM con matriz de covarianza diagonal y 2 estados ocultos
modelo_hmm = hmm.GaussianHMM(n_components=2, covariance_type="diag")
# Creamos una instancia del modelo HMM utilizando la clase GaussianHMM de la biblioteca hmmlearn.
# Especificamos que queremos utilizar una matriz de covarianza diagonal con covariance_type="diag".
# También especificamos que queremos 2 estados ocultos con n_components=2.

# Datos de entrada (secuencia de observaciones)
secuencia_observaciones = np.array([[1.0], [2.0], [3.0], [4.0], [5.0]])
# Creamos un arreglo numpy que contiene una secuencia de observaciones.
# Cada observación es un arreglo de una dimensión (un escalar) y representa un punto en nuestra secuencia de datos.

# Entrenamiento del modelo HMM
modelo_hmm.fit(secuencia_observaciones)
# Entrenamos el modelo HMM utilizando el método fit().
# Pasamos nuestra secuencia de observaciones como argumento para entrenar el modelo.

# Predicción del estado oculto y las observaciones
estados_ocultos_predichos = modelo_hmm.predict(secuencia_observaciones)
# Utilizamos el método predict() para predecir los estados ocultos correspondientes a la secuencia de observaciones.

observaciones_predichas, _ = modelo_hmm.sample(len(secuencia_observaciones))
# Utilizamos el método sample() para generar nuevas observaciones a partir del modelo entrenado.
# En este caso, generamos el mismo número de observaciones que el tamaño de nuestra secuencia original.

# Resultados
print("Estados ocultos predichos:", estados_ocultos_predichos)
print("Observaciones predichas:", observaciones_predichas)
# Imprimimos los estados ocultos y las observaciones predichas por el modelo.
