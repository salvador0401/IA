##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
### Importamos los símbolos y las funciones necesarias de SymPy
from sympy import symbols, Or, And, Not, to_cnf

### Definimos una función para obtener las variables de una expresión lógica
def obtener_variables(expresion):
    # Utilizamos el método free_symbols para obtener las variables en la expresión
    return list(expresion.free_symbols)

### Definimos una función para convertir una expresión lógica a su forma normal conjuntiva (FNC)
def forma_normal_conjuntiva(expresion):
    # Convertimos la expresión a FNC utilizando to_cnf
    fnc = to_cnf(expresion)
    return fnc

### Definimos los símbolos para usar en nuestras expresiones lógicas
P, Q, R = symbols('P Q R')

### Definimos una expresión lógica de ejemplo
expresion_logica = And(Or(P, Q), Or(Not(P), R))

### Obtenemos las variables presentes en la expresión lógica
variables = obtener_variables(expresion_logica)

### Convertimos la expresión lógica a su forma normal conjuntiva (FNC)
fnc = forma_normal_conjuntiva(expresion_logica)

### Imprimimos la expresión original, las variables y la forma normal conjuntiva
print("Expresión original:", expresion_logica)
print("Variables en la expresión:", variables)
print("Forma Normal Conjuntiva (FNC):", fnc)
