##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import nltk
from nltk import PCFG
from nltk import ViterbiParser

# Definir una gramática probabilística
gramatica_pcfg = PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    V -> "vio" [0.4] | "comió" [0.6]
    NP -> "Juan" [0.2] | "María" [0.3] | "Bob" [0.5]
    P -> "con" [1.0]
""")

# Crear un parser Viterbi con la gramática
parser = ViterbiParser(gramatica_pcfg)

# Ejemplo de una oración para analizar
oracion = "Juan vio Bob con María"

# Tokenizar la oración
tokens = nltk.word_tokenize(oracion)

# Realizar el análisis sintáctico
arboles = parser.parse(tokens)

# Imprimir los árboles de análisis sintáctico posibles
for arbol in arboles:
    print(arbol)
