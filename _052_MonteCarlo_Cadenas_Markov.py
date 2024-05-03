##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random

# Definimos la matriz de transición de la cadena de Markov
# En este ejemplo, usaremos una matriz de transición simétrica
transition_matrix = [[0.5, 0.5],
                     [0.5, 0.5]]

# Función para realizar una transición en la cadena de Markov
def transition(current_state):
    next_state = random.choices([0, 1], weights=transition_matrix[current_state])[0]
    return next_state

# Función de densidad de probabilidad (en este ejemplo, simplemente una distribución uniforme)
def pdf(state):
    return 0.5

# Función de Monte Carlo para generar muestras de la cadena de Markov
def monte_carlo_mcmc(num_samples):
    current_state = random.choice([0, 1])  # Seleccionamos un estado inicial aleatorio
    samples = []
    for _ in range(num_samples):
        proposed_state = transition(current_state)
        acceptance_ratio = pdf(proposed_state) / pdf(current_state)
        if random.random() < acceptance_ratio:
            current_state = proposed_state
        samples.append(current_state)
    return samples

# Número de muestras a generar
num_samples = 1000

# Generamos las muestras utilizando el método de Monte Carlo para cadenas de Markov
samples = monte_carlo_mcmc(num_samples)

# Imprimimos algunas muestras generadas
print("Algunas muestras generadas:", samples[:10])
