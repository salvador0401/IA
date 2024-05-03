##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np

class BusquedaPolitica():
    def __init__(self, n_estados, n_acciones, gamma=0.9, theta=1e-5):
        self.n_estados = n_estados  # Número de estados
        self.n_acciones = n_acciones  # Número de acciones
        self.gamma = gamma  # Factor de descuento
        self.theta = theta  # Umbral de convergencia
        self.V = np.zeros(n_estados)  # Valores de los estados

    def encontrar_politica(self, modelo_transiciones, recompensas):
        while True:
            delta = 0
            # Iterar sobre todos los estados
            for s in range(self.n_estados):
                v = self.V[s]  # Almacenar el valor actual del estado
                # Calcular el nuevo valor del estado como el máximo de los valores futuros
                self.V[s] = max([sum([p * (recompensas[s][a] + self.gamma * self.V[s1]) for (p, s1) in modelo_transiciones[s][a]]) for a in range(self.n_acciones)])
                # Calcular la diferencia de valores para verificar la convergencia
                delta = max(delta, abs(v - self.V[s]))
            # Comprobar si se ha alcanzado la convergencia
            if delta < self.theta:
                break

        # Construir la política óptima basada en los valores de los estados
        politica = np.zeros(self.n_estados, dtype=int)
        for s in range(self.n_estados):
            # Para cada estado, elegir la acción que maximice el valor esperado
            politica[s] = np.argmax([sum([p * (recompensas[s][a] + self.gamma * self.V[s1]) for (p, s1) in modelo_transiciones[s][a]]) for a in range(self.n_acciones)])

        return politica


# Ejemplo de uso
if __name__ == "__main__":
    # Definición de modelo de transiciones y recompensas
    n_estados = 3  # Número de estados
    n_acciones = 2  # Número de acciones

    # Modelo de transiciones: especifica las probabilidades de transición y los estados alcanzables dado un estado-acción
    modelo_transiciones = [
        # Estado 0
        [[(0.8, 0), (0.2, 1)],  # Acción 0
         [(0.1, 0), (0.9, 1)]],  # Acción 1
        # Estado 1
        [[(0.7, 0), (0.3, 2)],  # Acción 0
         [(0.5, 0), (0.5, 2)]],  # Acción 1
        # Estado 2
        [[(0.6, 2), (0.4, 2)],  # Acción 0
         [(0.0, 0), (1.0, 2)]]   # Acción 1
    ]

    # Recompensas: especifica las recompensas asociadas a cada estado-acción
    recompensas = [
        [-1, 0],  # Estado 0
        [-1, -1], # Estado 1
        [0, 1]    # Estado 2
    ]

    # Crear instancia de la clase BusquedaPolitica
    busqueda_politica = BusquedaPolitica(n_estados, n_acciones)

    # Encontrar la política óptima
    politica_optima = busqueda_politica.encontrar_politica(modelo_transiciones, recompensas)

    # Imprimir la política óptima encontrada
    print("Política óptima encontrada:", politica_optima)
