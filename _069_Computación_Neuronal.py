##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la biblioteca numpy para operaciones numéricas eficientes

# Definición de la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # La función de activación sigmoide retorna el valor de la función 1 / (1 + e^(-x))

# Definición de la neurona artificial
class Neurona:
    def __init__(self, pesos, sesgo):  # Método de inicialización de la clase Neurona
        self.pesos = pesos  # Inicializa los pesos de la neurona
        self.sesgo = sesgo  # Inicializa el sesgo de la neurona
    
    def feedforward(self, entrada):  # Método para calcular la salida de la neurona
        total = np.dot(self.pesos, entrada) + self.sesgo  # Calcula el total ponderado de las entradas más el sesgo
        return sigmoid(total)  # Aplica la función de activación sigmoide al total y retorna la salida de la neurona

# Pesos y sesgo para la neurona
pesos = np.array([0.5, -0.5])  # Define los pesos de las conexiones sinápticas
sesgo = 0.2  # Define el sesgo de la neurona

# Entrada para la neurona
entrada = np.array([0.3, 0.8])  # Define la entrada de la neurona

# Creación de la neurona
neurona = Neurona(pesos, sesgo)  # Crea una instancia de la clase Neurona con los pesos y sesgo dados

# Cálculo de la salida de la neurona
salida = neurona.feedforward(entrada)  # Calcula la salida de la neurona dada la entrada

# Impresión de la salida
print("Salida de la neurona:", salida)  # Imprime la salida de la neurona
