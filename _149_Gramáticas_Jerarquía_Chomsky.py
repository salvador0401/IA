##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import re  # Importa el módulo de expresiones regulares
import random  # Importa el módulo de generación de números aleatorios

class RegularGrammar:  # Definición de la clase RegularGrammar
    def __init__(self, productions):  # Método constructor que recibe las producciones de la gramática
        self.productions = productions  # Inicialización de las producciones de la gramática

    def generate_random_string(self, start_symbol, max_length=10):  # Método para generar una cadena aleatoria
        string = ""  # Inicialización de la cadena
        current_symbol = start_symbol  # Símbolo inicial

        while len(string) < max_length:  # Bucle mientras la longitud de la cadena sea menor que la longitud máxima
            if current_symbol not in self.productions:  # Si el símbolo actual no tiene producciones
                break  # Salir del bucle
            production = random.choice(self.productions[current_symbol])  # Selecciona una producción aleatoria para el símbolo actual
            string += production[1]  # Agrega el símbolo terminal de la producción a la cadena
            current_symbol = production[0]  # Actualiza el símbolo actual al siguiente símbolo no terminal de la producción

        return string  # Devuelve la cadena generada

    def is_valid(self, string, start_symbol):  # Método para verificar si una cadena es válida en la gramática
        stack = [(start_symbol, 0)]  # Inicialización de la pila con el símbolo inicial y el índice 0

        while stack:  # Bucle mientras la pila no esté vacía
            symbol, index = stack.pop()  # Desapila un símbolo y su índice
            if index == len(string):  # Si el índice es igual a la longitud de la cadena
                if symbol == start_symbol:  # Si el símbolo es el inicial
                    return True  # La cadena es válida
                continue  # Continuar con el siguiente símbolo de la pila

            if symbol in self.productions:  # Si el símbolo está en las producciones
                productions = self.productions[symbol]  # Obtiene las producciones del símbolo
                for production in productions:  # Itera sobre las producciones
                    if string[index:].startswith(production[1]):  # Si la cadena desde el índice coincide con el símbolo terminal de la producción
                        for char in reversed(production[0]):  # Agrega los símbolos no terminales de la producción a la pila en orden inverso
                            stack.append((char, index))
                        stack.append((symbol, index + len(production[1])))  # Agrega el símbolo actual y actualiza el índice
                        break  # Sale del bucle de producción actual
                else:  # Si no se encontró una producción que coincida
                    continue  # Continuar con el siguiente símbolo de la pila
            elif symbol == string[index]:  # Si el símbolo es igual al carácter en la posición del índice
                stack.append((start_symbol, index + 1))  # Agrega el símbolo inicial y actualiza el índice

        return False  # La cadena no es válida si se sale del bucle sin devolver True

# Ejemplo de uso
productions = {  # Producciones de la gramática
    'S': [('A', '0'), ('B', '1')],  # Producciones para el símbolo S
    'A': [('A', '0'), ('B', '1')],  # Producciones para el símbolo A
    'B': [('S', '1'), ('B', '0')]   # Producciones para el símbolo B
}

grammar = RegularGrammar(productions)  # Instancia de la clase RegularGrammar con las producciones dadas
print("Producciones de la gramática:")  # Imprime un encabezado
for symbol, productions in productions.items():  # Itera sobre los símbolos y sus producciones
    print(f"{symbol} -> {' | '.join([f'{x[0]}{x[1]}' for x in productions])}")  # Imprime las producciones de cada símbolo

# Generar una cadena aleatoria
random_string = grammar.generate_random_string('S')  # Genera una cadena aleatoria comenzando desde el símbolo S
print("\nCadena generada aleatoriamente:", random_string)  # Imprime la cadena generada aleatoriamente

# Comprobar si una cadena es válida
test_string = "001110"  # Cadena de prueba
if grammar.is_valid(test_string, 'S'):  # Verifica si la cadena es válida en la gramática empezando desde el símbolo S
    print("\nLa cadena es válida.")  # Imprime un mensaje si la cadena es válida
else:
    print("\nLa cadena no es válida.")  # Imprime un mensaje si la cadena no es válida
