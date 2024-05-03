##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la biblioteca numpy y la renombra como np

class Perceptron:  # Define la clase Perceptrón
    def __init__(self, num_inputs, learning_rate=0.01, epochs=100):  # Define el método de inicialización
        self.num_inputs = num_inputs  # Establece el número de entradas del perceptrón
        self.learning_rate = learning_rate  # Establece la tasa de aprendizaje
        self.epochs = epochs  # Establece el número de épocas
        self.weights = np.zeros(num_inputs + 1)  # Inicializa los pesos del perceptrón con ceros
    
    def predict(self, inputs):  # Define el método para hacer predicciones
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Calcula la suma ponderada de las entradas y los pesos
        return 1 if summation > 0 else 0  # Devuelve 1 si la suma es mayor que cero, de lo contrario, devuelve 0
    
    def train(self, training_inputs, labels):  # Define el método para entrenar el perceptrón
        for _ in range(self.epochs):  # Itera sobre el número de épocas
            for inputs, label in zip(training_inputs, labels):  # Itera sobre los datos de entrenamiento y las etiquetas
                prediction = self.predict(inputs)  # Realiza una predicción
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs  # Actualiza los pesos de las entradas
                self.weights[0] += self.learning_rate * (label - prediction)  # Actualiza el sesgo

class Adaline:  # Define la clase Adaline
    def __init__(self, num_inputs, learning_rate=0.01, epochs=100):  # Define el método de inicialización
        self.num_inputs = num_inputs  # Establece el número de entradas de Adaline
        self.learning_rate = learning_rate  # Establece la tasa de aprendizaje
        self.epochs = epochs  # Establece el número de épocas
        self.weights = np.zeros(num_inputs + 1)  # Inicializa los pesos de Adaline con ceros
        
    def predict(self, inputs):  # Define el método para hacer predicciones
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Calcula la suma ponderada de las entradas y los pesos
        return 1 if summation > 0 else 0  # Devuelve 1 si la suma es mayor que cero, de lo contrario, devuelve 0
    
    def train(self, training_inputs, labels):  # Define el método para entrenar Adaline
        for _ in range(self.epochs):  # Itera sobre el número de épocas
            for inputs, label in zip(training_inputs, labels):  # Itera sobre los datos de entrenamiento y las etiquetas
                prediction = self.predict(inputs)  # Realiza una predicción
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs  # Actualiza los pesos de las entradas
                self.weights[0] += self.learning_rate * (label - prediction)  # Actualiza el sesgo

class Madaline:  # Define la clase Madaline
    def __init__(self, num_inputs, num_outputs, learning_rate=0.01, epochs=100):  # Define el método de inicialización
        self.num_inputs = num_inputs  # Establece el número de entradas de Madaline
        self.num_outputs = num_outputs  # Establece el número de salidas de Madaline
        self.learning_rate = learning_rate  # Establece la tasa de aprendizaje
        self.epochs = epochs  # Establece el número de épocas
        self.weights = np.zeros((num_inputs + 1, num_outputs))  # Inicializa los pesos de Madaline con ceros
        
    def predict(self, inputs):  # Define el método para hacer predicciones
        summation = np.dot(inputs, self.weights[1:, :]) + self.weights[0, :]  # Calcula la suma ponderada de las entradas y los pesos
        return np.where(summation > 0, 1, 0)  # Devuelve 1 si la suma es mayor que cero, de lo contrario, devuelve 0
    
    def train(self, training_inputs, labels):  # Define el método para entrenar Madaline
        for _ in range(self.epochs):  # Itera sobre el número de épocas
            for inputs, label in zip(training_inputs, labels):  # Itera sobre los datos de entrenamiento y las etiquetas
                prediction = self.predict(inputs)  # Realiza una predicción
                self.weights[1:, :] += self.learning_rate * np.outer(inputs, (label - prediction))  # Actualiza los pesos de las entradas
                self.weights[0, :] += self.learning_rate * (label - prediction)  # Actualiza el sesgo

# Ejemplo de uso

# Datos de entrada
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Etiquetas
y_and = np.array([0, 0, 0, 1])
y_or = np.array([0, 1, 1, 1])
y_xor = np.array([0, 1, 1, 0])

# Perceptrón AND
print("Perceptrón AND:")
perceptron_and = Perceptron(num_inputs=2)  # Crea una instancia de Perceptrón para la operación AND
perceptron_and.train(X, y_and)  # Entrena el Perceptrón con los datos de entrada y las etiquetas
print("Pesos finales:", perceptron_and.weights)  # Imprime los pesos finales del Perceptrón
for i in range(len(X)):  # Itera sobre los datos de entrada
    print("Predicción para {}: {}".format(X[i], perceptron_and.predict(X[i])))  # Imprime las predicciones del Perceptrón para cada entrada

# Perceptrón OR
print("\nPerceptrón OR:")
perceptron_or = Perceptron(num_inputs=2)  # Crea una instancia de Perceptrón para la operación OR
perceptron_or.train(X, y_or)  # Entrena el Perceptrón con los datos de entrada y las etiquetas
print("Pesos finales:", perceptron_or.weights)  # Imprime los pesos finales del Perceptrón
for i in range(len(X)):  # Itera sobre los datos de entrada
    print("Predicción para {}: {}".format(X[i], perceptron_or.predict(X[i])))  # Imprime las predicciones del Perceptrón para cada entrada

# Adaline XOR
print("\nADALINE XOR:")
adaline_xor = Adaline(num_inputs=2)  # Crea una instancia de Adaline para la operación XOR
adaline_xor.train(X, y_xor)  # Entrena Adaline con los datos de entrada y las etiquetas
print("Pesos finales:", adaline_xor.weights)  # Imprime los pesos finales de Adaline
for i in range(len(X)):  # Itera sobre los datos de entrada
    print("Predicción para {}: {}".format(X[i], adaline_xor.predict(X[i])))  # Imprime las predicciones de Adaline para cada entrada

# MADALINE XOR
print("\nMADALINE XOR:")
madaline_xor = Madaline(num_inputs=2, num_outputs=1)  # Crea una instancia de Madaline para la operación XOR
madaline_xor.train(X, y_xor)  # Entrena Madaline con los datos de entrada y las etiquetas
print("Pesos finales:", madaline_xor.weights)  # Imprime los pesos finales de Madaline
for i in range(len(X)):  # Itera sobre los datos de entrada
    print("Predicción para {}: {}".format(X[i], madaline_xor.predict(X[i])))  # Imprime las predicciones de Madaline para cada entrada
