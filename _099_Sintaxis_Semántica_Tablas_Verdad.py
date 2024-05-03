##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import itertools  # Importa el módulo itertools para trabajar con iteradores y combinaciones.

def generate_truth_table(expression):  # Define una función llamada generate_truth_table que toma una expresión proposicional como argumento.
    variables = sorted(set(c for c in expression if c.isalpha()))  # Encuentra todas las letras únicas en la expresión y las ordena alfabéticamente.
    num_vars = len(variables)  # Calcula la cantidad de variables en la expresión.
    rows = list(itertools.product([False, True], repeat=num_vars))  # Genera todas las combinaciones de valores de verdad para las variables.

    print("Truth Table for expression:", expression)  # Imprime un encabezado para la tabla de verdad.
    print("-" * (4 * num_vars + 3))  # Imprime una línea divisoria.
    print("|", end="")  # Imprime el inicio de la fila de encabezados de variables.
    for var in variables:  # Itera sobre las variables.
        print(f" {var} |", end="")  # Imprime el nombre de cada variable.
    print(f" {expression} |")  # Imprime el nombre de la expresión al final de la fila.
    print("-" * (4 * num_vars + 3))  # Imprime otra línea divisoria.

    for row in rows:  # Itera sobre todas las filas de la tabla de verdad.
        row_eval = {var: val for var, val in zip(variables, row)}  # Crea un diccionario con los valores de verdad de las variables en esta fila.
        result = eval(expression, row_eval)  # Evalúa la expresión proposicional en esta fila.
        print("|", end="")  # Imprime el inicio de la fila.
        for val in row:  # Itera sobre los valores de verdad de las variables en esta fila.
            print(f" {val} |", end="")  # Imprime cada valor de verdad.
        print(f" {result} |")  # Imprime el resultado de evaluar la expresión en esta fila.
        print("-" * (4 * num_vars + 3))  # Imprime otra línea divisoria al final de la fila.

# Ejemplo de uso
if __name__ == "__main__":  # Verifica si el script está siendo ejecutado directamente.
    expression = '(p & q) | (~p)'  # Define una expresión proposicional de ejemplo.
    #input("Ingrese una expresión proposicional usando solo letras y los operadores lógicos (& para AND, | para OR, ~ para NOT, > para IMPLICA, y = para EQUIVALENCIA): ")
    generate_truth_table(expression)  # Genera la tabla de verdad para la expresión dada.
