##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la librería NumPy para operaciones numéricas

# Definición de la función de control proporcional (P)
def control_p(error, Kp):
    return Kp * error  # Retorna la corrección de velocidad proporcional al error

# Parámetros del control proporcional (P)
Kp = 0.1  # Ganancia proporcional

# Condiciones iniciales del robot
x_robot = 0  # Posición inicial en el eje x
y_robot = 0  # Posición inicial en el eje y
theta_robot = np.pi / 2  # Orientación inicial del robot (en radianes)
v_robot = 1  # Velocidad lineal del robot

# Parámetros del entorno y de la línea a seguir
x_linea = np.linspace(-5, 5, 100)  # Coordenadas x de la línea a seguir
y_linea = np.sin(x_linea)  # Coordenadas y de la línea a seguir

# Tiempo de simulación
dt = 0.1  # Paso de tiempo
t_simulacion = np.arange(0, 10, dt)  # Vector de tiempo

# Inicialización de variables
x_robot_hist = []  # Historial de posiciones en x del robot
y_robot_hist = []  # Historial de posiciones en y del robot

# Simulación del movimiento del robot siguiendo la línea
for t in t_simulacion:
    # Calcula el error como la diferencia entre la posición y la línea
    error = y_robot - np.interp(x_robot, x_linea, y_linea)
    
    # Calcula la corrección de velocidad utilizando el control proporcional
    correccion_velocidad = control_p(error, Kp)
    
    # Actualiza la posición del robot en función de su velocidad y orientación
    x_robot += v_robot * np.cos(theta_robot) * dt
    y_robot += v_robot * np.sin(theta_robot) * dt
    
    # Aplica la corrección de velocidad para ajustar la orientación del robot
    theta_robot -= correccion_velocidad * dt
    
    # Almacena las posiciones actuales del robot
    x_robot_hist.append(x_robot)
    y_robot_hist.append(y_robot)

# Visualización del movimiento del robot
import matplotlib.pyplot as plt  # Importa la librería Matplotlib para visualización

plt.figure(figsize=(8, 6))

# Grafica la línea a seguir
plt.plot(x_linea, y_linea, label='Línea a seguir', color='black')

# Grafica la trayectoria del robot
plt.plot(x_robot_hist, y_robot_hist, label='Trayectoria del robot', color='red')

# Configuración de la gráfica
plt.xlabel('Posición en x')
plt.ylabel('Posición en y')
plt.title('Movimiento del Robot Siguiendo una Línea')
plt.legend()
plt.grid(True)
plt.axis('equal')

plt.show()
