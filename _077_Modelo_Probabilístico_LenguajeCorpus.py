##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from collections import defaultdict  # Importa la clase defaultdict del módulo collections

class ModeloLenguajeNgram:
    def __init__(self, corpus, n):
        self.n = n  # Define el tamaño del n-grama
        self.contadores = defaultdict(int)  # Crea un diccionario de contadores para almacenar las frecuencias de los n-gramas
        self.contadores_contexto = defaultdict(int)  # Crea un diccionario de contadores para almacenar las frecuencias de los contextos
        self.entrenar(corpus)  # Entrena el modelo con el corpus proporcionado

    def entrenar(self, corpus):
        for oracion in corpus:  # Itera sobre cada oración en el corpus
            tokens = ['<s>'] * (self.n - 1) + oracion + ['</s>']  # Añade marcadores de inicio y fin de oración
            for i in range(self.n - 1, len(tokens)):  # Itera sobre los índices del corpus
                contexto = tuple(tokens[i - self.n + 1:i])  # Define el contexto del n-grama actual
                palabra = tokens[i]  # Obtiene la palabra actual del corpus
                self.contadores[(contexto, palabra)] += 1  # Incrementa el contador del n-grama específico
                self.contadores_contexto[contexto] += 1  # Incrementa el contador del contexto

    def probabilidad(self, contexto, palabra):
        return self.contadores[(contexto, palabra)] / self.contadores_contexto[contexto]  # Calcula la probabilidad de la palabra dado el contexto

# Ejemplo de corpus de texto
corpus = [
    ['el', 'gato', 'se', 'sentó', 'sobre', 'la', 'alfombra'],  # Primera oración del corpus
    ['el', 'perro', 'comió', 'el', 'hueso'],  # Segunda oración del corpus
    ['el', 'gato', 'persiguió', 'al', 'perro']  # Tercera oración del corpus
]

# Crear y entrenar el modelo de lenguaje con trigramas
modelo = ModeloLenguajeNgram(corpus, n=3)  # Crea una instancia del modelo de lenguaje N-gram con n=3

# Calcular la probabilidad de una palabra dado un contexto
contexto = ('el', 'gato')  # Define el contexto
palabra = 'se'  # Define la palabra
probabilidad = modelo.probabilidad(contexto, palabra)  # Calcula la probabilidad de la palabra dado el contexto
print(f"La probabilidad de '{palabra}' dado '{' '.join(contexto)}' es: {probabilidad:.4f}")  # Imprime la probabilidad calculada
