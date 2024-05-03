##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de palabras clave y símbolos
palabras_clave = {'if', 'else', 'while', 'for', 'int', 'float', 'return'}  # Conjunto de palabras clave reservadas
simbolos = {'(', ')', '{', '}', ';', ',', '+', '-', '*', '/'}  # Conjunto de símbolos

# Función para realizar el análisis léxico
def analisis_lexico(cadena):
    tokens = []  # Lista para almacenar los tokens encontrados
    palabra_actual = ''  # Variable para almacenar la palabra actual

    # Itera sobre cada caracter en la cadena
    for char in cadena:
        # Si el caracter es un espacio en blanco, verifica si hay una palabra actual
        if char.isspace():
            if palabra_actual:
                # Si la palabra actual es una palabra clave, agrégala como token
                if palabra_actual in palabras_clave:
                    tokens.append(('PALABRA_CLAVE', palabra_actual))
                else:
                    # De lo contrario, agrégala como identificador
                    tokens.append(('IDENTIFICADOR', palabra_actual))
                palabra_actual = ''  # Restablece la palabra actual
        # Si el caracter es un símbolo, verifica si hay una palabra actual
        elif char in simbolos:
            if palabra_actual:
                # Si hay una palabra actual, agrégala como identificador
                tokens.append(('IDENTIFICADOR', palabra_actual))
                palabra_actual = ''  # Restablece la palabra actual
            # Agrega el símbolo como token
            tokens.append(('SIMBOLO', char))
        else:
            # Agrega el caracter a la palabra actual
            palabra_actual += char
    
    # Verifica si hay una palabra actual después del bucle
    if palabra_actual:
        # Si la palabra actual es una palabra clave, agrégala como token
        if palabra_actual in palabras_clave:
            tokens.append(('PALABRA_CLAVE', palabra_actual))
        else:
            # De lo contrario, agrégala como identificador
            tokens.append(('IDENTIFICADOR', palabra_actual))

    return tokens

# Ejemplo de uso
entrada = "if (x > 0) { return x; } else { return -x; }"
tokens = analisis_lexico(entrada)
for token in tokens:
    print(token)
