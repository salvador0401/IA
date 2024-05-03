##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class SemanticAnalyzer:  # Definición de la clase SemanticAnalyzer
    def __init__(self):  # Método constructor de la clase
        self.keywords = {  # Creación de un diccionario de palabras clave y sus significados
            'comer': 'acción de ingerir alimentos',  # Palabra clave y su significado
            'dormir': 'estado de reposo del organismo',  # Palabra clave y su significado
            'correr': 'moverse rápidamente con los pies',  # Palabra clave y su significado
            'felicidad': 'estado emocional positivo',  # Palabra clave y su significado
            'tristeza': 'estado emocional negativo'  # Palabra clave y su significado
        }

    def analyze_sentence(self, sentence):  # Método para analizar una oración
        found_keywords = []  # Lista para almacenar las palabras clave encontradas

        for word in sentence.split():  # Iteración sobre cada palabra en la oración
            if word.lower() in self.keywords:  # Verifica si la palabra está en el diccionario de palabras clave
                found_keywords.append((word, self.keywords[word.lower()]))  # Agrega la palabra y su significado a la lista de resultados

        return found_keywords  # Retorna la lista de palabras clave encontradas junto con sus significados

# Ejemplo de uso
analyzer = SemanticAnalyzer()  # Instancia del analizador semántico
sentence = "Me gusta correr por la mañana porque me da felicidad."  # Oración de ejemplo
analysis_result = analyzer.analyze_sentence(sentence)  # Realiza el análisis semántico de la oración

print("Análisis Semántico:")  # Imprime un mensaje indicando el análisis semántico
for keyword, meaning in analysis_result:  # Iteración sobre las palabras clave encontradas y sus significados
    print(f"Palabra clave: {keyword}, Significado: {meaning}")  # Imprime la palabra clave y su significado
