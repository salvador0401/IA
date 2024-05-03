##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class AmbiguityResolver:  # Definimos la clase AmbiguityResolver
    def __init__(self):  # Definimos el método constructor de la clase
        pass  # No hay inicialización necesaria en este caso

    def resolve_ambiguity(self, sentence):  # Definimos el método para resolver la ambigüedad
        interpretations = []  # Creamos una lista para almacenar las interpretaciones posibles de la frase

        # Interpretación 1: "Vi a la mujer a través del telescopio."
        interpretation_1 = "Vi a la mujer a través del telescopio."
        interpretations.append(interpretation_1)  # Añadimos la interpretación a la lista de interpretaciones

        # Interpretación 2: "Vi a la mujer que estaba sosteniendo el telescopio."
        interpretation_2 = "Vi a la mujer que estaba sosteniendo el telescopio."
        interpretations.append(interpretation_2)  # Añadimos la interpretación a la lista de interpretaciones

        return interpretations  # Retornamos todas las interpretaciones posibles

# Ejemplo de uso
resolver = AmbiguityResolver()  # Creamos una instancia de la clase AmbiguityResolver

ambiguous_sentence = "Vi a la mujer con el telescopio."  # Definimos la frase ambigua
interpretations = resolver.resolve_ambiguity(ambiguous_sentence)  # Resolvemos la ambigüedad

print("Frase ambigua:", ambiguous_sentence)  # Imprimimos la frase ambigua
print("Interpretaciones:")  # Imprimimos un mensaje indicando las interpretaciones posibles
for i, interpretation in enumerate(interpretations, start=1):  # Iteramos sobre las interpretaciones posibles
    print(f"Interpretación {i}: {interpretation}")  # Imprimimos cada interpretación con su índice
