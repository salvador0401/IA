##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas eficientes

# Definición de la función de activación sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Definición de la función sigmoide

def sigmoid_derivative(x):
    return x * (1 - x)  # Derivada de la función sigmoide

# Datos de entrada y salida
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Matriz de entrada: características
y = np.array([[0], [1], [1], [0]])  # Matriz de salida: etiquetas

# Inicialización de pesos y sesgos
np.random.seed(1)  # Fijamos la semilla aleatoria para reproducibilidad
input_size = 2  # Tamaño de la capa de entrada
hidden_size = 4  # Tamaño de la capa oculta
output_size = 1  # Tamaño de la capa de salida
learning_rate = 0.1  # Tasa de aprendizaje para ajustar los pesos

# Pesos para la capa oculta y la capa de salida
weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))  # Pesos para la capa oculta
weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))  # Pesos para la capa de salida

# Sesgos para la capa oculta y la capa de salida
bias_hidden = np.random.uniform(size=(1, hidden_size))  # Sesgo para la capa oculta
bias_output = np.random.uniform(size=(1, output_size))  # Sesgo para la capa de salida

# Entrenamiento de la red neuronal utilizando retropropagación del error
epochs = 10000  # Número de épocas de entrenamiento
for epoch in range(epochs):  # Para cada época de entrenamiento
    # Forward propagation (propagación hacia adelante)
    hidden_input = np.dot(X, weights_input_hidden) + bias_hidden  # Entrada ponderada a la capa oculta
    hidden_output = sigmoid(hidden_input)  # Salida de la capa oculta
    output = np.dot(hidden_output, weights_hidden_output) + bias_output  # Entrada ponderada a la capa de salida
    predicted_output = sigmoid(output)  # Salida de la capa de salida
    
    # Cálculo del error
    error = y - predicted_output  # Error entre la salida deseada y la salida predicha
    
    # Backpropagation (retropropagación)
    output_delta = error * sigmoid_derivative(predicted_output)  # Delta de error en la capa de salida
    hidden_error = output_delta.dot(weights_hidden_output.T)  # Error en la capa oculta
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)  # Delta de error en la capa oculta
    
    # Actualización de pesos y sesgos
    weights_hidden_output += hidden_output.T.dot(output_delta) * learning_rate  # Actualización de pesos de la capa de salida
    weights_input_hidden += X.T.dot(hidden_delta) * learning_rate  # Actualización de pesos de la capa oculta
    bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate  # Actualización del sesgo de la capa de salida
    bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate  # Actualización del sesgo de la capa oculta

# Imprimir los resultados finales
print("Pesos de la capa oculta:")
print(weights_input_hidden)  # Imprimir los pesos de la capa oculta
print("\nPesos de la capa de salida:")
print(weights_hidden_output)  # Imprimir los pesos de la capa de salida
print("\nSesgo de la capa oculta:")
print(bias_hidden)  # Imprimir el sesgo de la capa oculta
print("\nSesgo de la capa de salida:")
print(bias_output)  # Imprimir el sesgo de la capa de salida

# Predicción final
print("\nPredicciones finales:")
print(predicted_output)  # Imprimir las predicciones finales
