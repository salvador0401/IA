##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class GrammarInduction:  # Definimos la clase GrammarInduction para la inducción gramatical
    def __init__(self):  # Definimos el método constructor de la clase
        self.examples = []  # Inicializamos una lista para almacenar los ejemplos de texto

    def add_example(self, example):  # Definimos el método para agregar un ejemplo
        self.examples.append(example)  # Agregamos el ejemplo a la lista de ejemplos

    def induce_grammar(self):  # Definimos el método para inducir la gramática a partir de los ejemplos
        if not self.examples:  # Verificamos si hay ejemplos
            return "No hay ejemplos para inducir la gramática."  # Si no hay ejemplos, retornamos un mensaje indicando la ausencia de ejemplos

        grammar = {}  # Creamos un diccionario para almacenar la gramática inducida
        for example in self.examples:  # Iteramos sobre cada ejemplo
            words = example.split()  # Dividimos el ejemplo en palabras
            for i in range(len(words) - 1):  # Iteramos sobre cada palabra en el ejemplo, excepto la última
                current_word = words[i]  # Obtenemos la palabra actual
                next_word = words[i + 1]  # Obtenemos la palabra siguiente

                if current_word not in grammar:  # Verificamos si la palabra actual no está en la gramática
                    grammar[current_word] = []  # Si no está, creamos una entrada para la palabra actual en la gramática

                if next_word not in grammar[current_word]:  # Verificamos si la palabra siguiente no está en las opciones de palabras siguientes para la palabra actual
                    grammar[current_word].append(next_word)  # Si no está, la agregamos a las opciones de palabras siguientes para la palabra actual

        return grammar  # Retornamos la gramática inducida como un diccionario

# Ejemplo de uso
inductor = GrammarInduction()  # Creamos una instancia de la clase GrammarInduction

# Agregamos ejemplos
inductor.add_example("El gato persigue al ratón")
inductor.add_example("La niña juega con la pelota")

# Realizamos la inducción de la gramática
grammar = inductor.induce_grammar()

# Mostramos la gramática inducida
print("Gramática Inducida:")
for key, value in grammar.items():
    print(f"{key} -> {' | '.join(value)}")  # Imprimimos las reglas gramaticales inducidas
