##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import nltk  # Importa la librería NLTK para el procesamiento del lenguaje natural
import numpy as np  # Importa la librería NumPy para operaciones numéricas eficientes

# Descargar los recursos necesarios de NLTK (solo si no los tienes descargados ya)
nltk.download('punkt')  # Descarga los recursos de tokenización
nltk.download('averaged_perceptron_tagger')  # Descarga los recursos de etiquetado POS

# Datos de entrenamiento (frases en dos idiomas)
sentences_en = [
    "the cat",
    "the dog",
    "a dog",
    "your dog",
    "your cat",
    "and"
]

sentences_es = [
    "el gato",
    "el perro",
    "un perro",
    "tu perro",
    "tu gato",
    "y"
]

# Tokenización y etiquetado POS (Part-of-Speech) de las frases
en_tokens = [nltk.word_tokenize(sent) for sent in sentences_en]  # Tokeniza las frases en inglés
es_tokens = [nltk.word_tokenize(sent) for sent in sentences_es]  # Tokeniza las frases en español

en_tagged = [nltk.pos_tag(tokens) for tokens in en_tokens]  # Etiqueta POS las frases en inglés
es_tagged = [nltk.pos_tag(tokens) for tokens in es_tokens]  # Etiqueta POS las frases en español

# Crear diccionarios de palabras y etiquetas
en_words = set(word for sent in en_tokens for word in sent)  # Crea un conjunto de palabras en inglés
es_words = set(word for sent in es_tokens for word in sent)  # Crea un conjunto de palabras en español

en_tags = set(tag for sent in en_tagged for _, tag in sent)  # Crea un conjunto de etiquetas POS en inglés
es_tags = set(tag for sent in es_tagged for _, tag in sent)  # Crea un conjunto de etiquetas POS en español

# Crear matrices de probabilidades de traducción de palabras
translation_probs = np.zeros((len(en_words), len(es_words)))  # Crea una matriz de ceros para las probabilidades de traducción

for en_sent, es_sent in zip(en_tagged, es_tagged):  # Recorre las frases etiquetadas en inglés y español
    for (en_word, en_tag), (es_word, es_tag) in zip(en_sent, es_sent):  # Recorre las palabras y etiquetas en ambas frases
        en_index = list(en_words).index(en_word)  # Obtiene el índice de la palabra en inglés
        es_index = list(es_words).index(es_word)  # Obtiene el índice de la palabra en español
        translation_probs[en_index, es_index] += 1  # Incrementa la cuenta de la traducción

# Normalizar las probabilidades
translation_probs /= translation_probs.sum(axis=1, keepdims=True)  # Normaliza las probabilidades de traducción

# Función para traducir una frase de inglés a español
def translate(sentence):
    tokens = nltk.word_tokenize(sentence)  # Tokeniza la frase de entrada
    tagged = nltk.pos_tag(tokens)  # Etiqueta POS las palabras de la frase
    translation = []  # Inicializa la lista de traducción

    for token, tag in tagged:  # Recorre las palabras y etiquetas de la frase etiquetada
        en_index = list(en_words).index(token)  # Obtiene el índice de la palabra en inglés
        es_index = np.argmax(translation_probs[en_index])  # Obtiene el índice de la traducción con mayor probabilidad
        translation.append(list(es_words)[es_index])  # Agrega la palabra traducida a la lista de traducción

    return " ".join(translation)  # Devuelve la traducción como una cadena de texto

# Ejemplo de uso
input_sentence = "a cat and a dog"  # Definición de la frase de entrada
output_sentence = translate(input_sentence)  # Traducción de la frase de entrada
print("Input:", input_sentence)  # Imprime la frase de entrada
print("Translated:", output_sentence)  # Imprime la traducción de la frase
