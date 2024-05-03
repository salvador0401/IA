##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def probabilidad_conjunta(prob_A, prob_B_dado_A, prob_C_dado_B):
    """
    Calcula la probabilidad conjunta de los eventos A, B y C utilizando la regla de la cadena.
    """
    prob_B = prob_B_dado_A * prob_A  # P(B) = P(B|A) * P(A)
    prob_C = prob_C_dado_B * prob_B  # P(C) = P(C|B) * P(B)
    return prob_C

# Probabilidad de los eventos individuales
prob_A = 0.5
prob_B_dado_A = 0.7
prob_C_dado_B = 0.4

# Calculamos la probabilidad conjunta de los eventos A, B y C
prob_conjunta = probabilidad_conjunta(prob_A, prob_B_dado_A, prob_C_dado_B)

print("La probabilidad conjunta de los eventos A, B y C es:", prob_conjunta)
