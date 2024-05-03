##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definimos las probabilidades a priori
prob_urna1 = 0.5
prob_urna2 = 0.5

# Definimos las probabilidades condicionales: P(Color | Urna)
prob_color_dado_urna1 = {'rojo': 0.2, 'verde': 0.4, 'azul': 0.4}
prob_color_dado_urna2 = {'rojo': 0.5, 'verde': 0.3, 'azul': 0.2}

# Función para calcular la probabilidad usando la regla de Bayes
def calcular_probabilidad_bayes(color, urna):
    # Verificamos la urna seleccionada y obtenemos la probabilidad condicional correspondiente
    if urna == 1:
        prob_color_dado_urna = prob_color_dado_urna1[color]
        prob_urna = prob_urna1
    else:
        prob_color_dado_urna = prob_color_dado_urna2[color]
        prob_urna = prob_urna2
    
    # Aplicamos la regla de Bayes para calcular la probabilidad de que la bola sea de ese color y de esa urna
    prob_color = prob_color_dado_urna * prob_urna
    return prob_color

def main():
    color_elegido = 'verde'  # Color elegido
    urna_elegida = 1  # Urna elegida

    # Calculamos la probabilidad usando la regla de Bayes
    probabilidad = calcular_probabilidad_bayes(color_elegido, urna_elegida)

    # Imprimimos el resultado
    print(f"La probabilidad de que la bola verde provenga de la urna {urna_elegida} es: {probabilidad}")

if __name__ == "__main__":
    main()
