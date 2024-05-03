##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from sympy import symbols, Not, Or, And, Implies, satisfiable
from sympy.logic.boolalg import to_cnf

# Definir los símbolos
A, B = symbols('A B')  # Define los símbolos lógicos A y B

# Definir las cláusulas
clauses = [
    Or(A, B),  # La cláusula A OR B
    Or(A),     # La cláusula A
    Or(B)      # La cláusula B
]

# Convertir a la forma normal conjuntiva (CNF)
cnf = to_cnf(And(*clauses))  # Convierte las cláusulas a CNF

# Mostrar la forma normal conjuntiva
print("Forma normal conjuntiva (CNF):", cnf)

# Comprobar satisfacibilidad
if satisfiable(cnf):
    print("La fórmula es satisfacible.")  # Si la fórmula es satisfacible, imprime este mensaje
else:
    print("La fórmula no es satisfacible.")  # Si la fórmula no es satisfacible, imprime este mensaje

