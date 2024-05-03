##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def unify_var(var, x, theta):

    # Si la variable ya está en el sustituto theta, unifica su valor con x.
    if var in theta:
        return unify(theta[var], x, theta)
    # Si x ya está en el sustituto theta, unifica var con su valor.
    elif x in theta:
        return unify(var, theta[x], theta)
    # Si no se ha encontrado ninguna coincidencia, asigna el valor de x a var en el sustituto theta.
    else:
        theta[var] = x
        return theta

def unify(x, y, theta):

    # Si el sustituto theta es None, la unificación no es posible, devuelve None.
    if theta is None:
        return None
    # Si los términos x e y son idénticos, no hay necesidad de hacer nada, devuelve theta.
    elif x == y:
        return theta
    # Si x es una variable, unifica x con y usando la función unify_var.
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, theta)
    # Si y es una variable, unifica y con x usando la función unify_var.
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, theta)
    # Si ambos x e y son listas, unifica cada elemento correspondiente de x e y recursivamente.
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):  # Si las listas tienen longitudes diferentes, la unificación no es posible.
            return None
        else:
            for xi, yi in zip(x, y):
                theta = unify(xi, yi, theta)  # Llama a unify recursivamente para cada par de elementos.
            return theta
    # Si no se cumple ninguna de las condiciones anteriores, la unificación no es posible, devuelve None.
    else:
        return None

# Ejemplo de uso
x = ['P', 'x', 'y']
y = ['P', 'A', 'B']
theta = {}

resultado = unify(x, y, theta)
print(resultado)
