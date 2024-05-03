##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de tokens
tokens = [
    ('NUMERO', r'\d+'),            # Token para representar números enteros
    ('SUMA', r'\+'),               # Token para representar la operación de suma
    ('RESTA', r'\-'),              # Token para representar la operación de resta
    ('MULTIPLICACION', r'\*'),     # Token para representar la operación de multiplicación
    ('DIVISION', r'\/'),           # Token para representar la operación de división
    ('PARENTESIS_IZQ', r'\('),     # Token para representar el paréntesis izquierdo
    ('PARENTESIS_DER', r'\)'),     # Token para representar el paréntesis derecho
]

# Función para realizar el análisis sintáctico
def parse(tokens):
    # Función interna para manejar los factores
    def factor():
        token = tokens.pop(0)      # Toma y elimina el primer token de la lista
        if token[0] == 'NUMERO':   # Si el token es un número
            return float(token[1]) # Convierte y devuelve el valor del número
        elif token[0] == 'PARENTESIS_IZQ':  # Si el token es un paréntesis izquierdo
            resultado = expression()        # Evalúa la expresión dentro de los paréntesis
            tokens.pop(0)                   # Elimina el paréntesis derecho
            return resultado

    # Función interna para manejar los términos
    def term():
        resultado = factor()    # Obtiene el primer factor
        # Mientras haya tokens y el primer token sea multiplicación o división
        while tokens and tokens[0][0] in ('MULTIPLICACION', 'DIVISION'):
            operador = tokens.pop(0)  # Toma y elimina el operador
            if operador[0] == 'MULTIPLICACION':  # Si el operador es multiplicación
                resultado *= factor()            # Multiplica por el siguiente factor
            else:                                # Si el operador es división
                divisor = factor()               # Obtiene el divisor
                if divisor != 0:                 # Si el divisor no es cero
                    resultado /= divisor         # Divide por el divisor
                else:                            # Si el divisor es cero
                    raise ValueError("División por cero")  # Genera un error
        return resultado

    # Función interna para manejar las expresiones
    def expression():
        resultado = term()        # Obtiene el primer término
        # Mientras haya tokens y el primer token sea suma o resta
        while tokens and tokens[0][0] in ('SUMA', 'RESTA'):
            operador = tokens.pop(0)  # Toma y elimina el operador
            if operador[0] == 'SUMA':  # Si el operador es suma
                resultado += term()    # Suma el siguiente término
            else:                      # Si el operador es resta
                resultado -= term()    # Resta el siguiente término
        return resultado

    return expression()  # Devuelve el resultado de la evaluación de la expresión

# Ejemplo de uso
entrada = "3 + 4 * (2 - 1)"  # Define una expresión aritmética
# Define una lista de tokens para la expresión
tokens = [('NUMERO', '3'), ('SUMA', '+'), ('NUMERO', '4'), ('MULTIPLICACION', '*'), 
          ('PARENTESIS_IZQ', '('), ('NUMERO', '2'), ('RESTA', '-'), ('NUMERO', '1'), 
          ('PARENTESIS_DER', ')')]
resultado = parse(tokens)  # Realiza el análisis sintáctico y la evaluación de la expresión
print("El resultado de la expresión es:", resultado)  # Imprime el resultado
