##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random

# Definición de la función objetivo (en este caso, buscamos el número objetivo)
def funcion_objetivo(numero_buscar, numero_aleatorio):
    if numero_aleatorio == numero_buscar:
        return True
    else:
        return False

# Implementación de la Búsqueda Online
def busqueda_online(numero_buscar, max_intentos):
    intentos = 0
    encontrado = False
    
    while intentos < max_intentos and not encontrado:
        # Genera un número aleatorio como supuesta solución
        numero_aleatorio = random.randint(1, 30)
        
        # Evalúa si la supuesta solución es la solución correcta
        encontrado = funcion_objetivo(numero_buscar, numero_aleatorio)
        
        # Incrementa el contador de intentos
        intentos += 1
    
    return encontrado, intentos

# Parámetros
numero_a_buscar = 5
max_intentos = 20

# Ejecución de la búsqueda online
resultado, intentos_realizados = busqueda_online(numero_a_buscar, max_intentos)

# Imprime el resultado
if resultado:
    print(f"¡El número {numero_a_buscar} fue encontrado en {intentos_realizados} intentos!")
else:
    print(f"El número {numero_a_buscar} no fue encontrado después de {intentos_realizados} intentos.")
