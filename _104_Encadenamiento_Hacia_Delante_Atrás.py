##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definimos una función para el encadenamiento hacia adelante
def encadenamiento_hacia_adelante(base_hechos, reglas):
    while True:
        algo_cambiado = False
        # Iteramos sobre todas las reglas
        for regla in reglas:
            # Verificamos si todos los antecedentes de la regla están en la base de hechos
            antecedentes_verdaderos = all(premisa in base_hechos for premisa in regla[0])
            consecuente = regla[1]
            # Si todos los antecedentes son verdaderos y el consecuente no está en la base de hechos, lo agregamos
            if antecedentes_verdaderos and consecuente not in base_hechos:
                base_hechos.append(consecuente)
                algo_cambiado = True
        # Si no se agregaron nuevos hechos en esta iteración, terminamos el bucle
        if not algo_cambiado:
            break
    # Devolvemos la base de hechos final
    return base_hechos

# Definimos una función para el encadenamiento hacia atrás
def encadenamiento_hacia_atras(meta, reglas, base_hechos):
    # Si la meta ya está en la base de hechos, devolvemos True
    if meta in base_hechos:
        return True
    # Si la meta no está en la base de hechos, intentamos probarla utilizando las reglas
    for regla in reglas:
        consecuente = regla[1]
        if meta == consecuente:
            antecedentes = regla[0]
            # Verificamos si todos los antecedentes pueden demostrarse recursivamente
            if all(encadenamiento_hacia_atras(premisa, reglas, base_hechos) for premisa in antecedentes):
                return True
    # Si ninguna regla puede demostrar la meta, devolvemos False
    return False

# Base de hechos inicial
base_hechos = ['P', 'Q']

# Definición de reglas
reglas = [(['P'], 'R'),
          (['R'], 'S'),
          (['Q'], 'T'),
          (['S', 'T'], 'U')]

# Encadenamiento hacia adelante
print("Encadenamiento hacia adelante:")
resultado_adelante = encadenamiento_hacia_adelante(base_hechos, reglas)
print("Base de hechos final:", resultado_adelante)

# Encadenamiento hacia atrás
print("\nEncadenamiento hacia atrás:")
meta = 'U'
resultado_atras = encadenamiento_hacia_atras(meta, reglas, base_hechos)
print("¿Se puede demostrar la meta?", resultado_atras)
