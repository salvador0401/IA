##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la biblioteca numpy para operaciones numéricas
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para visualización
import tensorflow as tf  # Importa la biblioteca TensorFlow para redes neuronales
from tensorflow.keras.models import Sequential  # Importa la clase Sequential para crear modelos secuenciales
from tensorflow.keras.layers import Dense  # Importa la capa Dense para capas totalmente conectadas

# Generar datos de ejemplo para un problema de separabilidad lineal
np.random.seed(0)  # Fija la semilla aleatoria para reproducibilidad
num_samples = 200  # Número de muestras de datos
X = np.random.normal(loc=0, scale=1, size=(num_samples, 2))  # Genera características de entrada con distribución normal
y = (X[:, 0] + X[:, 1] > 0).astype(int)  # Etiquetas: 1 si la suma de las características es positiva, 0 en otro caso

# Visualizar los datos
plt.figure(figsize=(8, 6))  # Configura el tamaño de la figura
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', marker='o', edgecolors='k')  # Grafica los puntos de acuerdo a las etiquetas
plt.title('Datos de ejemplo para separabilidad lineal')  # Establece el título del gráfico
plt.xlabel('Característica 1')  # Etiqueta del eje x
plt.ylabel('Característica 2')  # Etiqueta del eje y
plt.show()  # Muestra el gráfico

# Definir el modelo de red neuronal
model = Sequential([  # Crea un modelo secuencial
    Dense(1, activation='sigmoid', input_shape=(2,))  # Agrega una capa densa con una neurona y función de activación sigmoide
])

# Compilar el modelo
model.compile(optimizer='adam',  # Configura el optimizador Adam
              loss='binary_crossentropy',  # Configura la función de pérdida de entropía cruzada binaria
              metrics=['accuracy'])  # Configura la métrica de precisión

# Entrenar el modelo
history = model.fit(X, y, epochs=100, verbose=0)  # Entrena el modelo en los datos de entrada y etiquetas

# Graficar la pérdida durante el entrenamiento
plt.figure(figsize=(8, 6))  # Configura el tamaño de la figura
plt.plot(history.history['loss'])  # Grafica la pérdida durante el entrenamiento
plt.title('Pérdida durante el entrenamiento')  # Establece el título del gráfico
plt.xlabel('Época')  # Etiqueta del eje x
plt.ylabel('Pérdida')  # Etiqueta del eje y
plt.show()  # Muestra el gráfico

# Evaluar el modelo en los datos de entrenamiento
loss, accuracy = model.evaluate(X, y)  # Evalúa el modelo en los datos de entrada y etiquetas
print(f'Precisión en los datos de entrenamiento: {accuracy:.2f}')  # Imprime la precisión del modelo
