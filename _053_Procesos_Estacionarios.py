##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importamos la biblioteca NumPy para operaciones numéricas
import matplotlib.pyplot as plt  # Importamos la biblioteca Matplotlib para graficar

# Definición de parámetros del proceso estacionario
mean = 0  # Media del proceso estacionario
std_dev = 1  # Desviación estándar del proceso estacionario
num_samples = 1000  # Número de muestras del proceso
num_steps = 100  # Número de pasos en el tiempo

# Generar muestras del proceso estacionario
samples = np.random.normal(mean, std_dev, size=(num_samples, num_steps))
# Genera una matriz de muestras aleatorias usando una distribución normal con media y desviación estándar especificadas

# Calcular la media y la varianza a través del tiempo
mean_over_time = np.mean(samples, axis=0)  # Calcula la media a través del tiempo
variance_over_time = np.var(samples, axis=0)  # Calcula la varianza a través del tiempo

# Graficar la media y la varianza a través del tiempo
time_steps = np.arange(num_steps)  # Crea una matriz de pasos de tiempo
plt.figure(figsize=(10, 6))  # Establece el tamaño de la figura
plt.plot(time_steps, mean_over_time, label='Media')  # Grafica la evolución de la media en función del tiempo
plt.plot(time_steps, variance_over_time, label='Varianza')  # Grafica la evolución de la varianza en función del tiempo
plt.xlabel('Tiempo')  # Etiqueta del eje x
plt.ylabel('Valor')  # Etiqueta del eje y
plt.title('Evolución de la Media y la Varianza en un Proceso Estacionario')  # Título de la gráfica
plt.legend()  # Muestra la leyenda
plt.grid(True)  # Muestra una cuadrícula en el gráfico
plt.show()  # Muestra la gráfica
