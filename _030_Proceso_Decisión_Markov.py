##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la librería NumPy

class MDP:  # Define una clase para el Proceso de Decisión de Markov (MDP)
    def __init__(self, n_states, n_actions, transition_probs, rewards, gamma=0.9):
        """
        Inicializa el MDP.

        Args:
            n_states (int): Número de estados.
            n_actions (int): Número de acciones.
            transition_probs (numpy.array): Matriz de probabilidades de transición.
            rewards (numpy.array): Matriz de recompensas.
            gamma (float): Factor de descuento.
        """
        self.n_states = n_states  # Guarda el número de estados en el MDP
        self.n_actions = n_actions  # Guarda el número de acciones en el MDP
        self.transition_probs = transition_probs  # Guarda la matriz de probabilidades de transición
        self.rewards = rewards  # Guarda la matriz de recompensas
        self.gamma = gamma  # Guarda el factor de descuento

    def value_iteration(self, epsilon=0.0001):
        """
        Realiza el algoritmo de iteración de valor para encontrar la política óptima.

        Args:
            epsilon (float): Umbral de convergencia.

        Returns:
            numpy.array: Política óptima.
        """
        V = np.zeros(self.n_states)  # Inicializa los valores de los estados a 0
        while True:  # Bucle hasta que se alcance la convergencia
            delta = 0  # Variable para rastrear el cambio máximo en los valores de los estados
            for s in range(self.n_states):  # Itera sobre cada estado en el MDP
                v = V[s]  # Almacena el valor actual del estado
                # Calcula el valor de un estado como el máximo valor esperado sobre todas las acciones posibles
                V[s] = max(self.calculate_q_value(s, a, V) for a in range(self.n_actions))
                delta = max(delta, abs(v - V[s]))  # Actualiza el cambio máximo
            if delta < epsilon:  # Si la diferencia entre los valores de los estados es menor que epsilon, se detiene
                break

        # Calcula la política óptima a partir de los valores de los estados
        policy = np.zeros((self.n_states, self.n_actions))
        for s in range(self.n_states):
            # Encuentra la mejor acción para cada estado según los valores actuales de los estados
            best_action = np.argmax([self.calculate_q_value(s, a, V) for a in range(self.n_actions)])
            policy[s, best_action] = 1  # Asigna probabilidad 1 a la mejor acción
        return policy

    def calculate_q_value(self, state, action, V):
        """
        Calcula el valor Q para un par (estado, acción).

        Args:
            state (int): Estado.
            action (int): Acción.
            V (numpy.array): Valores de los estados.

        Returns:
            float: Valor Q.
        """
        # Calcula el valor Q para el par (estado, acción) utilizando la ecuación de Bellman
        return sum(self.transition_probs[state, action, next_state] * (self.rewards[state, action, next_state] + self.gamma * V[next_state]) for next_state in range(self.n_states))


# Definición del MDP de ejemplo
n_states = 3  # Número de estados
n_actions = 2  # Número de acciones
transition_probs = np.array([[[0.7, 0.3, 0.0], [1.0, 0.0, 0.0]], [[0.0, 1.0, 0.0], [0.8, 0.2, 0.0]], [[0.8, 0.2, 0.0], [0.0, 0.0, 1.0]]])
rewards = np.array([[[10, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, -50]]])
mdp = MDP(n_states, n_actions, transition_probs, rewards)

# Ejecución del algoritmo de iteración de valor para obtener la política óptima
optimal_policy = mdp.value_iteration()

print("Política óptima:")
print(optimal_policy)
