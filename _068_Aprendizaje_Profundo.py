##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import tensorflow as tf  # Importa la biblioteca TensorFlow y la renombra como tf
from tensorflow.keras import Sequential  # Importa la clase Sequential del módulo keras dentro de TensorFlow
from tensorflow.keras.layers import Dense  # Importa la capa Dense del módulo layers dentro de keras en TensorFlow

# Definición del modelo de red neuronal
modelo = Sequential([  # Crea un modelo secuencial de capas
    Dense(64, activation='relu', input_shape=(10,)),  # Agrega una capa densa con 64 unidades y función de activación ReLU como la primera capa con entrada de forma (10,)
    Dense(64, activation='relu'),  # Agrega una segunda capa densa con 64 unidades y función de activación ReLU
    Dense(1, activation='sigmoid')  # Agrega una capa densa con 1 unidad y función de activación sigmoide
])

# Compilación del modelo
modelo.compile(optimizer='adam',  # Compila el modelo con el optimizador Adam
               loss='binary_crossentropy',  # Usa la función de pérdida binary_crossentropy
               metrics=['accuracy'])  # Utiliza la métrica de precisión (accuracy)

# Datos de ejemplo
X_train = tf.random.normal(shape=(1000, 10))  # Genera datos de entrada de forma aleatoria con distribución normal
y_train = tf.random.uniform(shape=(1000, 1), minval=0, maxval=2, dtype=tf.int32)  # Genera etiquetas de forma aleatoria con distribución uniforme

# Entrenamiento del modelo
modelo.fit(X_train, y_train, epochs=10, batch_size=32)  # Entrena el modelo durante 10 épocas con un tamaño de lote de 32

# Evaluación del modelo
loss, accuracy = modelo.evaluate(X_train, y_train)  # Evalúa el modelo con los datos de entrenamiento
print("Precisión del modelo:", accuracy)  # Imprime la precisión del modelo
