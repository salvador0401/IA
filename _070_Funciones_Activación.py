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

# Definición de las funciones de activación
def sigmoid(x):  # Define la función de activación sigmoide
    return 1 / (1 + np.exp(-x))

def relu(x):  # Define la función de activación ReLU
    return np.maximum(0, x)

def tanh(x):  # Define la función de activación tangente hiperbólica (tanh)
    return np.tanh(x)

def softmax(x):  # Define la función de activación softmax
    exp_values = np.exp(x - np.max(x, axis=0))  # Calcula los valores exponenciales de x
    return exp_values / np.sum(exp_values, axis=0)  # Calcula la función softmax de los valores exponenciales

# Datos de entrada
x = np.linspace(-5, 5, 100)  # Genera 100 puntos equidistantes entre -5 y 5 como valores de entrada

# Aplicación de las funciones de activación a los datos de entrada
y_sigmoid = sigmoid(x)  # Aplica la función sigmoide a los datos de entrada
y_relu = relu(x)  # Aplica la función ReLU a los datos de entrada
y_tanh = tanh(x)  # Aplica la función tangente hiperbólica (tanh) a los datos de entrada
y_softmax = softmax(x)  # Aplica la función softmax a los datos de entrada

# Visualización de las funciones de activación
plt.figure(figsize=(10, 6))  # Crea una nueva figura con tamaño 10x6 pulgadas

plt.plot(x, y_sigmoid, label='Sigmoid', color='blue')  # Grafica la función sigmoide
plt.plot(x, y_relu, label='ReLU', color='red')  # Grafica la función ReLU
plt.plot(x, y_tanh, label='Tanh', color='green')  # Grafica la función tangente hiperbólica (tanh)
plt.plot(x, y_softmax, label='Softmax', color='purple')  # Grafica la función softmax

plt.title('Funciones de Activación')  # Establece el título del gráfico como 'Funciones de Activación'
plt.xlabel('x')  # Etiqueta el eje x como 'x'
plt.ylabel('y')  # Etiqueta el eje y como 'y'
plt.legend()  # Muestra la leyenda
plt.grid(True)  # Muestra la cuadrícula en el gráfico
plt.show()  # Muestra el gráfico

