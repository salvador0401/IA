##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np

class MarkovChain:
    def __init__(self, transition_matrix, states):
      # Inicializa la cadena de Markov con la matriz de transición y los estados.

        self.transition_matrix = transition_matrix
        self.states = states
        self.num_states = len(states)

    def next_state(self, current_state):
       #Calcula el próximo estado de acuerdo con la matriz de transición.
    
        return np.random.choice(self.states, p=self.transition_matrix[current_state])

    def generate_states(self, start_state, num_steps):
       # Genera una secuencia de estados de acuerdo con la matriz de transición.

        current_state = start_state
        states_sequence = [current_state]
        for _ in range(num_steps - 1):
            current_state = self.next_state(current_state)
            states_sequence.append(current_state)
        return states_sequence

# Definición de la matriz de transición y los estados
transition_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])  # Ejemplo de matriz de transición
states = [0, 1]  # Ejemplo de estados: 0 y 1

# Crear la cadena de Markov
markov_chain = MarkovChain(transition_matrix, states)

# Generar una secuencia de estados a partir de un estado inicial
start_state = 0  # Estado inicial
num_steps = 10  # Número de pasos en el tiempo
states_sequence = markov_chain.generate_states(start_state, num_steps)

print("Secuencia de estados generada por la cadena de Markov:")
print(states_sequence)
