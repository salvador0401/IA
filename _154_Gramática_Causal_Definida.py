##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random  # Importamos el módulo random para generar números aleatorios

class CausalGrammar:  # Definimos la clase CausalGrammar
    def __init__(self):  # Definimos el método constructor de la clase
        # Listas de sujetos, verbos y objetos
        self.subjects = ['El gato', 'El perro', 'La tortuga', 'El pájaro', 'El pez']
        self.verbs = ['persiguió', 'atrapó', 'comió', 'miró', 'asustó']
        self.objects = ['el ratón', 'la mariposa', 'la comida', 'la pelota', 'la presa']

    def generate_sentence(self):  # Definimos el método para generar una oración
        subject = random.choice(self.subjects)  # Seleccionamos aleatoriamente un sujeto
        verb = random.choice(self.verbs)  # Seleccionamos aleatoriamente un verbo
        obj = random.choice(self.objects)  # Seleccionamos aleatoriamente un objeto

        return f"{subject} {verb} {obj} porque {self._generate_cause()}."  # Concatenamos las partes de la oración con una causa

    def _generate_cause(self):  # Definimos un método privado para generar una causa
        # Lista de posibles causas
        causes = [
            "estaba hambriento",
            "quería jugar",
            "se sintió amenazado",
            "escuchó un ruido",
            "vio movimiento"
        ]
        return random.choice(causes)  # Seleccionamos aleatoriamente una causa

# Ejemplo de uso
grammar = CausalGrammar()  # Creamos una instancia de la clase CausalGrammar

for _ in range(5):  # Generamos 5 oraciones
    sentence = grammar.generate_sentence()  # Generamos una oración
    print(sentence)  # Imprimimos la oración
