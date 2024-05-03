##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np

# Definimos la matriz de transición de estados
matriz_transicion = np.array([[0.8, 0.1, 0.1],  # Soleado -> Soleado, Nublado, Lluvioso
                               [0.2, 0.6, 0.2],  # Nublado -> Soleado, Nublado, Lluvioso
                               [0.3, 0.3, 0.4]]) # Lluvioso -> Soleado, Nublado, Lluvioso

# Definimos los estados
estados = ['Soleado', 'Nublado', 'Lluvioso']

# Función para predecir el clima futuro
def predecir_clima_actual(estado_actual):
    estado_futuro = np.random.choice(estados, p=matriz_transicion[estado_actual])
    return estado_futuro

def main():
    # Definimos el estado actual
    estado_actual = np.random.randint(0, 3)  # Seleccionamos un estado inicial aleatorio
    
    # Imprimimos el estado actual
    print("Estado actual:", estados[estado_actual])
    
    # Predecimos y mostramos el clima futuro para los próximos 5 días
    for i in range(1, 6):
        print(f"Día {i}: {predecir_clima_actual(estado_actual)}")
        estado_actual = estados.index(predecir_clima_actual(estado_actual))

if __name__ == "__main__":
    main()
