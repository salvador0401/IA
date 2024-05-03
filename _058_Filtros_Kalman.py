##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importamos la biblioteca NumPy para operaciones matriciales

class FiltroKalman:
    def __init__(self, x0, P0, A, Q, H, R):
        self.x = x0  # Estado inicial
        self.P = P0  # Covarianza inicial
        self.A = A    # Matriz de transición de estado
        self.Q = Q    # Covarianza del proceso
        self.H = H    # Matriz de observación
        self.R = R    # Covarianza de la observación

    def predict(self):
        # Predicción del siguiente estado
        self.x = np.dot(self.A, self.x)  # Actualizamos el estado prediciendo el siguiente estado
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q  # Actualizamos la covarianza

    def update(self, z):
        # Actualización del estado basado en la observación
        y = z - np.dot(self.H, self.x)  # Calculamos la diferencia entre la observación y la predicción
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R  # Calculamos la covarianza de la innovación
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))  # Calculamos la ganancia de Kalman
        self.x = self.x + np.dot(K, y)  # Actualizamos el estado usando la ganancia de Kalman
        self.P = self.P - np.dot(np.dot(K, self.H), self.P)  # Actualizamos la covarianza

# Definir las matrices y vectores necesarios para el filtro de Kalman
dt = 1.0  # Intervalo de tiempo entre mediciones
A = np.array([[1, dt], [0, 1]])  # Matriz de transición de estado (modelo de movimiento)
H = np.array([[1, 0]])           # Matriz de observación (modelo de medición)
Q = np.array([[0.1, 0], [0, 0.1]])  # Covarianza del proceso (ruido del proceso)
R = np.array([[1]])                 # Covarianza de la observación (ruido de la medición)

# Condiciones iniciales
x0 = np.array([[0], [0]])  # Estado inicial (posición y velocidad)
P0 = np.eye(2)             # Covarianza inicial (incertidumbre inicial)

# Crear el filtro de Kalman
filtro_kalman = FiltroKalman(x0, P0, A, Q, H, R)

# Simular un objeto moviéndose y realizar la estimación con el filtro de Kalman
observaciones = [1, 2, 3, 4, 5]  # Observaciones de posición del objeto
for z in observaciones:
    filtro_kalman.predict()        # Predicción del siguiente estado
    filtro_kalman.update(np.array([[z]]))  # Actualización basada en la observación
    print("Estimación de posición:", filtro_kalman.x[0, 0])  # Mostrar la estimación de posición
