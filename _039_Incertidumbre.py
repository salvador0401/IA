##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random

def lanzamiento_moneda():
    # Simula el lanzamiento de una moneda.
    # Devuelve 'Cara' o 'Cruz'.
    resultado = random.choice(['Cara', 'Cruz'])
    return resultado

def calcular_probabilidad(n_lanzamientos, resultado_deseado):
    # Realiza n_lanzamientos y calcula la probabilidad de obtener el resultado deseado.
    conteo_resultado_deseado = 0
    for _ in range(n_lanzamientos):
        resultado = lanzamiento_moneda()
        if resultado == resultado_deseado:
            conteo_resultado_deseado += 1
    
    probabilidad = conteo_resultado_deseado / n_lanzamientos
    return probabilidad

# Parámetros del juego
n_lanzamientos = 1000
resultado_deseado = 'Cara'

# Calcula la probabilidad de obtener 'Cara' en n_lanzamientos
probabilidad_cara = calcular_probabilidad(n_lanzamientos, resultado_deseado)

# Imprime el resultado
print(f"Después de {n_lanzamientos} lanzamientos, la probabilidad de obtener '{resultado_deseado}' es: {probabilidad_cara}")
