##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np

# Regla de Hebb para ajustar los pesos
def hebb_rule(x):
    return np.outer(x, x)

# Datos de entrada
x1 = np.array([1, -1, 1])
x2 = np.array([-1, 1, -1])

# Calcula los pesos usando la regla de Hebb
weights = hebb_rule(x1) + hebb_rule(x2)
print("Pesos ajustados con la regla de Hebb:\n", weights)
