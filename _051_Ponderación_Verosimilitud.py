##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random

# Definimos la función para simular lanzamientos de una moneda
def lanzar_moneda(probabilidad_caras):
    """
    Simula el lanzamiento de una moneda sesgada hacia caras.
    Retorna True si sale cara, False si sale cruz.
    """
    if random.random() < probabilidad_caras:
        return True
    else:
        return False

# Definimos la función para calcular la verosimilitud de los datos observados
def calcular_verosimilitud(datos, probabilidad_caras):
    """
    Calcula la verosimilitud de una secuencia de lanzamientos de moneda
    dada una cierta probabilidad de que la moneda sea justa.
    """
    verosimilitud = 1.0
    for resultado in datos:
        if resultado:  # Si es cara
            verosimilitud *= probabilidad_caras
        else:          # Si es cruz
            verosimilitud *= 1 - probabilidad_caras
    return verosimilitud

# Definimos la función para actualizar la probabilidad a posteriori
def actualizar_probabilidad_a_posteriori(probabilidad_previa, verosimilitud, constante_de_normalizacion):
    """
    Actualiza la probabilidad a posteriori utilizando la ponderación de verosimilitud.
    """
    return (probabilidad_previa * verosimilitud) / constante_de_normalizacion

# Parámetros iniciales
probabilidad_previa = 0.5  # Probabilidad a priori de que la moneda sea justa
probabilidad_real_caras = 0.6  # Probabilidad real de que la moneda salga cara
num_lanzamientos = 10  # Número de lanzamientos

# Simulamos una secuencia de lanzamientos de la moneda
datos_observados = [lanzar_moneda(probabilidad_real_caras) for _ in range(num_lanzamientos)]

# Calculamos la verosimilitud de los datos observados
verosimilitud = calcular_verosimilitud(datos_observados, probabilidad_real_caras)

# Calculamos la constante de normalización
constante_de_normalizacion = verosimilitud * probabilidad_previa + (1 - verosimilitud) * (1 - probabilidad_previa)

# Actualizamos la probabilidad a posteriori
probabilidad_posteriori = actualizar_probabilidad_a_posteriori(probabilidad_previa, verosimilitud, constante_de_normalizacion)

# Mostramos los resultados
print("Secuencia de lanzamientos observada:", datos_observados)
print("Verosimilitud de los datos observados:", verosimilitud)
print("Probabilidad a posteriori de que la moneda sea justa:", probabilidad_posteriori)
