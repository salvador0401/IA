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
import tensorflow as tf  # Importa la biblioteca tensorflow y la renombra como tf
from tensorflow.keras.models import Sequential  # Importa la clase Sequential del módulo models dentro de tensorflow.keras
from tensorflow.keras.layers import Dense  # Importa la capa Dense del módulo layers dentro de tensorflow.keras

# Función para generar datos de ejemplo (círculos concéntricos)
def generate_data(n_samples):
    theta = np.random.uniform(0, 2*np.pi, n_samples)  # Genera ángulos aleatorios uniformemente distribuidos
    r1 = np.random.uniform(0, 1, n_samples)  # Genera radios aleatorios uniformemente distribuidos para el círculo interno
    r2 = np.random.uniform(1, 2, n_samples)  # Genera radios aleatorios uniformemente distribuidos para el círculo externo
    x_inner = r1 * np.cos(theta)  # Calcula las coordenadas x del círculo interno
    y_inner = r1 * np.sin(theta)  # Calcula las coordenadas y del círculo interno
    x_outer = r2 * np.cos(theta)  # Calcula las coordenadas x del círculo externo
    y_outer = r2 * np.sin(theta)  # Calcula las coordenadas y del círculo externo
    X = np.vstack([np.column_stack([x_inner, y_inner]), np.column_stack([x_outer, y_outer])])  # Apila las coordenadas de los círculos internos y externos
    y = np.hstack([np.zeros(n_samples), np.ones(n_samples)])  # Genera etiquetas para los círculos internos y externos
    return X, y  # Devuelve los datos de entrada y las etiquetas

# Función para visualizar los datos de ejemplo
def plot_data(X, y):
    plt.figure(figsize=(6, 6))  # Crea una nueva figura con tamaño 6x6 pulgadas
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', marker='o', edgecolors='k')  # Grafica los datos de entrada con colores según las etiquetas
    plt.title('Datos de ejemplo')  # Establece el título del gráfico como 'Datos de ejemplo'
    plt.xlabel('Característica 1')  # Etiqueta el eje x como 'Característica 1'
    plt.ylabel('Característica 2')  # Etiqueta el eje y como 'Característica 2'
    plt.show()  # Muestra el gráfico

# Generar datos de ejemplo
X, y = generate_data(500)  # Genera 500 puntos de datos de ejemplo y sus etiquetas
plot_data(X, y)  # Visualiza los datos de ejemplo

# Definir el modelo de red neuronal multicapa
model = Sequential([  # Crea un modelo secuencial de capas
    Dense(64, activation='relu', input_shape=(2,)),  # Agrega una capa oculta con 64 neuronas y activación ReLU como la primera capa con entrada de forma (2,)
    Dense(1, activation='sigmoid')  # Agrega una capa de salida con 1 neurona y activación sigmoide
])

# Compilar el modelo
model.compile(optimizer='adam',  # Compila el modelo con el optimizador Adam
              loss='binary_crossentropy',  # Usa la función de pérdida binary_crossentropy
              metrics=['accuracy'])  # Utiliza la métrica de precisión (accuracy)

# Entrenar el modelo
history = model.fit(X, y, epochs=50, verbose=1, validation_split=0.2)  # Entrena el modelo durante 50 épocas con un tamaño de lote de 32

# Visualizar la pérdida durante el entrenamiento
plt.figure(figsize=(8, 6))  # Crea una nueva figura con tamaño 8x6 pulgadas
plt.plot(history.history['loss'], label='Pérdida en entrenamiento')  # Grafica la pérdida en entrenamiento
plt.plot(history.history['val_loss'], label='Pérdida en validación')  # Grafica la pérdida en validación
plt.title('Pérdida durante el entrenamiento')  # Establece el título del gráfico como 'Pérdida durante el entrenamiento'
plt.xlabel('Época')  # Etiqueta el eje x como 'Época'
plt.ylabel('Pérdida')  # Etiqueta el eje y como 'Pérdida'
plt.legend()  # Muestra la leyenda
plt.show()  # Muestra el gráfico

