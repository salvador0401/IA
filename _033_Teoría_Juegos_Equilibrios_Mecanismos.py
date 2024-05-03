##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de la función que simula el juego del dilema del prisionero
def dilema_del_prisionero(jugador1, jugador2):
    # Diccionario que mapea las combinaciones de elecciones a las recompensas
    recompensas = {
        ("cooperar", "cooperar"): (3, 3),        # Ambos cooperan, ambos reciben una recompensa alta
        ("cooperar", "traicionar"): (0, 5),      # Jugador 1 coopera, Jugador 2 traiciona, Jugador 1 recibe la peor recompensa y Jugador 2 la mejor
        ("traicionar", "cooperar"): (5, 0),      # Jugador 1 traiciona, Jugador 2 coopera, Jugador 1 recibe la mejor recompensa y Jugador 2 la peor
        ("traicionar", "traicionar"): (1, 1)    # Ambos traicionan, ambos reciben una recompensa baja
    }
    # Obtener las recompensas para las elecciones dadas
    recompensa_jugador1, recompensa_jugador2 = recompensas[(jugador1, jugador2)]
    return recompensa_jugador1, recompensa_jugador2

# Función principal del programa
def main():
    print("Bienvenido al dilema del prisionero.")
    print("Jugador 1, ¿cooperar (c) o traicionar (t)?")
    eleccion_jugador1 = input().strip().lower()   # Obtener la elección del jugador 1 y limpiarla
    print("Jugador 2, ¿cooperar (c) o traicionar (t)?")
    eleccion_jugador2 = input().strip().lower()   # Obtener la elección del jugador 2 y limpiarla

    # Validar las elecciones de los jugadores
    if eleccion_jugador1 not in ["c", "t"] or eleccion_jugador2 not in ["c", "t"]:
        print("Por favor, introduce 'c' para cooperar o 't' para traicionar.")
        return

    # Convertir las elecciones a texto para una mejor legibilidad
    if eleccion_jugador1 == "c":
        eleccion_jugador1_texto = "cooperar"
    else:
        eleccion_jugador1_texto = "traicionar"

    if eleccion_jugador2 == "c":
        eleccion_jugador2_texto = "cooperar"
    else:
        eleccion_jugador2_texto = "traicionar"

    # Llamar a la función que simula el juego y obtener las recompensas
    recompensa_jugador1, recompensa_jugador2 = dilema_del_prisionero(eleccion_jugador1_texto, eleccion_jugador2_texto)
    # Mostrar las recompensas para cada jugador
    print(f"Jugador 1 obtiene {recompensa_jugador1} puntos.")
    print(f"Jugador 2 obtiene {recompensa_jugador2} puntos.")

# Verificar si el script se está ejecutando directamente y llamar a la función principal
if __name__ == "__main__":
    main()
