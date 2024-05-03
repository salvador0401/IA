##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np

# Función de activación de la red de Hopfield
def hopfield_activation(x, weights):
    return np.sign(np.dot(weights, x))

# Datos de entrada y pesos
x = np.array([1, -1, 1])
weights = np.array([[0, 1, -1],
                    [1, 0, -1],
                    [-1, -1, 0]])

# Calcula la activación de la red de Hopfield
activation = hopfield_activation(x, weights)
print("Activación de la red de Hopfield:", activation)
