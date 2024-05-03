##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter:
    def __init__(self, A, B, H, Q, R, initial_state):
        # Inicializa el Filtro de Kalman con los parámetros del modelo y el estado inicial.
        self.A = A  # Matriz de transición de estado
        self.B = B  # Matriz de control
        self.H = H  # Matriz de observación
        self.Q = Q  # Covarianza del ruido de proceso
        self.R = R  # Covarianza del ruido de medición
        self.state = initial_state  # Estado inicial
        self.covariance = np.eye(len(initial_state))  # Covarianza inicial

    def predict(self, control_input=None):
               # Predice el siguiente estado.
   
        if control_input is not None:
            self.state = np.dot(self.A, self.state) + np.dot(self.B, control_input)
        else:
            self.state = np.dot(self.A, self.state)
        self.covariance = np.dot(np.dot(self.A, self.covariance), self.A.T) + self.Q

    def update(self, measurement):

       # Actualiza el estado basado en la medición.
        innovation = measurement - np.dot(self.H, self.state)
        innovation_covariance = np.dot(np.dot(self.H, self.covariance), self.H.T) + self.R
        kalman_gain = np.dot(np.dot(self.covariance, self.H.T), np.linalg.inv(innovation_covariance))
        self.state += np.dot(kalman_gain, innovation)
        self.covariance = np.dot(np.eye(len(self.state)) - np.dot(kalman_gain, self.H), self.covariance)

# Parámetros del modelo del sistema
dt = 0.1  # Intervalo de tiempo entre las actualizaciones
A = np.array([[1, dt], [0, 1]])  # Matriz de transición de estado
B = np.array([[0.5*dt**2], [dt]])  # Matriz de control
H = np.array([[1, 0]])  # Matriz de observación
Q = np.array([[0.1, 0], [0, 0.1]])  # Covarianza del ruido de proceso
R = np.array([[1]])  # Covarianza del ruido de medición

# Estado inicial y medición inicial
initial_state = np.array([0, 0])  # [posición, velocidad]
initial_measurement = np.array([0])  # Posición medida inicialmente

# Crear el Filtro de Kalman
kf = KalmanFilter(A, B, H, Q, R, initial_state)

# Simulación de movimiento y medición
num_steps = 100
true_positions = []
measurements = []
filtered_positions = []

for i in range(num_steps):
    true_position = 0.5 * 9.8 * dt**2 * i**2  # Movimiento simulado del objeto (caída libre)
    measurement = true_position + np.random.normal(0, 1)  # Simular medición con ruido gaussiano
    kf.predict()  # Predicción del siguiente estado
    kf.update(measurement)  # Actualización del estado basado en la medición
    true_positions.append(true_position)
    measurements.append(measurement)
    filtered_positions.append(kf.state[0])

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(range(num_steps), true_positions, label='Posición Verdadera')
plt.plot(range(num_steps), measurements, label='Medición Ruidosa', marker='o', linestyle='', color='r')
plt.plot(range(num_steps), filtered_positions, label='Posición Filtrada', linestyle='--', color='g')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtro de Kalman: Predicción y Estimación de Posición')
plt.legend()
plt.grid(True)
plt.show()
