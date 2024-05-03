##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Se importan las bibliotecas necesarias de NLTK
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

# Se descargan los recursos necesarios para la tokenización y las stopwords en español
nltk.download('punkt')
nltk.download('stopwords')

# Se define el texto de ejemplo
texto = "La inteligencia artificial es el futuro. Hoy en día, muchos investigadores trabajan en el campo de la IA para mejorar nuestras vidas."

# Se tokeniza el texto en palabras
tokens = word_tokenize(texto.lower())

# Se crea un conjunto de stopwords en español
stop_words = set(stopwords.words('spanish'))

# Se filtran las stopwords y se eliminan los caracteres no alfanuméricos
filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

# Se inicializa un objeto Stemmer para realizar el stemming
stemmer = PorterStemmer()

# Se realiza stemming en las palabras filtradas
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Se calcula la frecuencia de cada palabra
freq_dist = FreqDist(stemmed_tokens)

# Se imprimen las 5 palabras más frecuentes
print(freq_dist.most_common(5))
