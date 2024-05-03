##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la librería NumPy para operaciones numéricas

# Definición de la función de predicción del filtro de Kalman extendido (EKF)
def prediccion(x, P, F, Q):
    x_prediccion = np.dot(F, x)  # Predice el nuevo estado utilizando la matriz de transición de estado F
    P_prediccion = np.dot(F, np.dot(P, F.T)) + Q  # Predice la nueva covarianza del estado
    return x_prediccion, P_prediccion

# Definición de la función de actualización del filtro de Kalman extendido (EKF)
def actualización(x_prediccion, P_prediccion, z, H, R):
    y = z - np.dot(H, x_prediccion)  # Calcula la innovación entre la medición y la predicción
    S = np.dot(H, np.dot(P_prediccion, H.T)) + R  # Calcula la matriz de covarianza de la innovación
    K = np.dot(P_prediccion, np.dot(H.T, np.linalg.inv(S)))  # Calcula la ganancia de Kalman
    x_actualizado = x_prediccion + np.dot(K, y)  # Actualiza el estado estimado
    P_actualizado = P_prediccion - np.dot(K, np.dot(H, P_prediccion))  # Actualiza la covarianza del estado
    return x_actualizado, P_actualizado

# Parámetros del filtro de Kalman extendido (EKF)
dt = 0.1  # Intervalo de tiempo entre cada actualización
F = np.array([[1, dt], [0, 1]])  # Matriz de transición de estado (modelo dinámico del sistema)
H = np.array([[1, 0]])  # Matriz de observación (relaciona el estado con las observaciones)
Q = np.array([[0.1, 0], [0, 0.01]])  # Covarianza del proceso (incertidumbre del modelo)
R = np.array([[1]])  # Covarianza de la medición (incertidumbre de las observaciones)

# Condiciones iniciales del filtro de Kalman extendido (EKF)
x = np.array([0, 0])  # Estado inicial (posición y velocidad)
P = np.array([[1, 0], [0, 1]])  # Covarianza inicial del estado

# Datos de la medición (en este ejemplo, solo se proporciona la posición)
mediciones = [1, 2, 3, 4, 5]

# Inicialización de las listas para almacenar los resultados
resultados_estado = []
resultados_covarianza = []

# Aplicar el filtro de Kalman extendido (EKF) para cada medición
for z in mediciones:
    # Predicción del estado siguiente
    x_prediccion, P_prediccion = prediccion(x, P, F, Q)
    
    # Actualización del estado basada en la medición
    x, P = actualización(x_prediccion, P_prediccion, z, H, R)
    
    # Almacenar los resultados de la estimación del estado y la covarianza
    resultados_estado.append(x)
    resultados_covarianza.append(P)

# Imprimir los resultados de la estimación
for i in range(len(mediciones)):
    print("Medición:", mediciones[i])
    print("Estado estimado:", resultados_estado[i])
    print("Covarianza del estado:", resultados_covarianza[i])
    print()
