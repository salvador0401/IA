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

# Función para calcular la distribución de probabilidad de la suma de dos dados
def distribucion_probabilidad_dados():
    # Inicializa un array de ceros para almacenar las frecuencias de cada suma posible (2 a 12)
    probabilidades = np.zeros(11)

    # Ciclos anidados para simular el lanzamiento de dos dados
    for i in range(1, 7):  # Recorre los valores del primer dado (1 a 6)
        for j in range(1, 7):  # Recorre los valores del segundo dado (1 a 6)
            suma = i + j  # Calcula la suma de los valores de los dados
            probabilidades[suma-2] += 1  # Incrementa la frecuencia de la suma en el array de probabilidades

    probabilidades /= 36  # Normaliza las frecuencias para obtener probabilidades, dividiendo por el total de casos posibles
    return probabilidades

def main():
    valores = np.arange(2, 13)  # Valores posibles de la suma de dos dados (2 a 12)
    probabilidades = distribucion_probabilidad_dados()  # Calcula la distribución de probabilidad de la suma de dos dados

    # Visualización de la distribución de probabilidad como un gráfico de barras
    plt.bar(valores, probabilidades)  # Crea un gráfico de barras con los valores y probabilidades
    plt.title('Distribución de Probabilidad de la Suma de Dos Dados')  # Título del gráfico
    plt.xlabel('Suma de los Dados')  # Etiqueta del eje x
    plt.ylabel('Probabilidad')  # Etiqueta del eje y
    plt.xticks(valores)  # Establece los ticks del eje x en los valores posibles de la suma
    plt.show()  # Muestra el gráfico

if __name__ == "__main__":
    main()
