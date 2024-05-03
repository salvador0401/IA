##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Importamos la librería numpy para cálculos numéricos
import numpy as np

# Definimos una función para calcular la probabilidad condicionada
def probabilidad_condicionada(evento_a, evento_b):
    """
    Calcula la probabilidad condicionada P(A|B) dada P(A∩B) y P(B).
    """
    return evento_a / evento_b

# Definimos una función para normalizar un conjunto de datos
def normalizar(datos):
    """
    Normaliza un conjunto de datos para que tengan media 0 y desviación estándar 1.
    """
    media = np.mean(datos)
    desviacion_estandar = np.std(datos)
    datos_normalizados = (datos - media) / desviacion_estandar
    return datos_normalizados

# Ejemplo de cálculo de probabilidad condicionada
# Supongamos que P(B) = 0.6 y P(A∩B) = 0.3
probabilidad_b = 0.6
probabilidad_a_interseccion_b = 0.3

# Calculamos P(A|B)
probabilidad_a_dado_b = probabilidad_condicionada(probabilidad_a_interseccion_b, probabilidad_b)
print("La probabilidad condicionada P(A|B) es:", probabilidad_a_dado_b)

# Ejemplo de normalización de datos
# Supongamos que tenemos un conjunto de datos
datos = np.array([1, 2, 3, 4, 5])

# Normalizamos los datos
datos_normalizados = normalizar(datos)
print("Datos normalizados:", datos_normalizados)
