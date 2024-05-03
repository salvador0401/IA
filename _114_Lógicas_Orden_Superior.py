##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from functools import reduce

# Definición de funciones de lógica de orden superior

# Función de AND
def AND(*args):
    return reduce(lambda x, y: x and y, args)

# Función de OR
def OR(*args):
    return reduce(lambda x, y: x or y, args)

# Función de NOT
def NOT(x):
    return not x

# Función de IMPLICACIÓN
def IMPLIES(x, y):
    return (not x) or y

# Función de EQUIVALENCIA
def EQUIV(x, y):
    return (x and y) or ((not x) and (not y))

# Ejemplo de uso de lógica de orden superior

# Definimos algunos valores de prueba
p = True
q = False
r = True

# Probando las funciones lógicas
print("AND(p, q, r) =", AND(p, q, r))  # Salida esperada: False
print("OR(p, q, r) =", OR(p, q, r))     # Salida esperada: True
print("NOT(p) =", NOT(p))               # Salida esperada: False
print("IMPLIES(p, q) =", IMPLIES(p, q)) # Salida esperada: False
print("EQUIV(p, q) =", EQUIV(p, q))     # Salida esperada: False
