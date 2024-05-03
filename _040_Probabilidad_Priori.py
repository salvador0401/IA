##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def probabilidad_a_priori(evento, espacio_muestral):
    # Calcula la probabilidad a priori de un evento dado el espacio muestral.
    conteo_evento = sum(1 for e in espacio_muestral if e in evento)
    return conteo_evento / len(espacio_muestral)

def main():
    # Espacio muestral de lanzar un dado
    espacio_muestral = [1, 2, 3, 4, 5, 6]

    # Evento de interés: obtener un número par
    evento_par = [2, 4, 6]

    # Calcula la probabilidad a priori del evento de obtener un número par
    p_a_priori_par = probabilidad_a_priori(evento_par, espacio_muestral)

    # Imprime el resultado
    print("Probabilidad a priori de obtener un número par:", p_a_priori_par)

if __name__ == "__main__":
    main()
