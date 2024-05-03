##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np

# Función de activación de la red de Hamming
def hamming_activation(x, weights):
    return np.dot(x, weights)

# Datos de entrada y pesos
x = np.array([1, -1, 1])
weights = np.array([[1, -1, 1],
                    [-1, 1, -1],
                    [1, -1, 1]])

# Calcula la activación de la red de Hamming
activation = hamming_activation(x, weights)
print("Activación de la red de Hamming:", activation)
