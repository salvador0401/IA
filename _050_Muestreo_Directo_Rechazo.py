##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random  # Importa la biblioteca random para generar números aleatorios
import math    # Importa la biblioteca math para realizar operaciones matemáticas

# Función para estimar pi utilizando muestreo directo
def estimar_pi_muestreo_directo(num_puntos):
    puntos_dentro_circulo = 0  # Inicializa el contador de puntos dentro del círculo
    for _ in range(num_puntos):  # Repite el proceso para generar num_puntos puntos aleatorios
        x = random.uniform(0, 1)  # Genera una coordenada x aleatoria en el rango [0, 1)
        y = random.uniform(0, 1)  # Genera una coordenada y aleatoria en el rango [0, 1)
        distancia_al_centro = math.sqrt(x**2 + y**2)  # Calcula la distancia al centro del punto generado
        if distancia_al_centro <= 1:  # Si la distancia es menor o igual a 1, el punto está dentro del círculo
            puntos_dentro_circulo += 1  # Incrementa el contador de puntos dentro del círculo
    return 4 * puntos_dentro_circulo / num_puntos  # Devuelve la estimación de pi

# Función para estimar pi utilizando muestreo por rechazo
def estimar_pi_muestreo_por_rechazo(num_puntos):
    puntos_dentro_circulo = 0  # Inicializa el contador de puntos dentro del círculo
    puntos_totales = 0  # Inicializa el contador de puntos totales generados
    while puntos_totales < num_puntos:  # Repite el proceso hasta generar num_puntos puntos
        x = random.uniform(0, 1)  # Genera una coordenada x aleatoria en el rango [0, 1)
        y = random.uniform(0, 1)  # Genera una coordenada y aleatoria en el rango [0, 1)
        distancia_al_centro = math.sqrt(x**2 + y**2)  # Calcula la distancia al centro del punto generado
        if distancia_al_centro <= 1:  # Si la distancia es menor o igual a 1, el punto está dentro del círculo
            puntos_dentro_circulo += 1  # Incrementa el contador de puntos dentro del círculo
        puntos_totales += 1  # Incrementa el contador de puntos totales generados
    return 4 * puntos_dentro_circulo / puntos_totales  # Devuelve la estimación de pi

# Número de puntos para la estimación de pi
num_puntos = 100000

# Estimación de pi utilizando muestreo directo
pi_estimado_directo = estimar_pi_muestreo_directo(num_puntos)
print("Estimación de pi utilizando muestreo directo:", pi_estimado_directo)

# Estimación de pi utilizando muestreo por rechazo
pi_estimado_rechazo = estimar_pi_muestreo_por_rechazo(num_puntos)
print("Estimación de pi utilizando muestreo por rechazo:", pi_estimado_rechazo)
