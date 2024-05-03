##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np

# Función de activación de la máquina de Boltzmann
def boltzmann_activation(x, weights, bias):
    energy = -0.5 * np.dot(np.dot(x, weights), x) - np.dot(bias, x)
    return 1 / (1 + np.exp(-2 * energy))

# Datos de entrada, pesos y sesgo
x = np.array([1, -1, 1])
weights = np.array([[0, 1, -1],
                    [1, 0, -1],
                    [-1, -1, 0]])
bias = np.array([0, 0, 0])

# Calcula la activación de la máquina de Boltzmann
activation = boltzmann_activation(x, weights, bias)
print("Activación de la máquina de Boltzmann:", activation)
