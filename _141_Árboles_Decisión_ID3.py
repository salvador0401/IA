##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import math  # Importa el módulo math para utilizar funciones matemáticas

# Definición de la clase Nodo para el árbol de decisión
class Nodo:  # Define una clase llamada Nodo
    def __init__(self, valor):  # Define el método de inicialización de la clase Nodo con el atributo valor
        self.valor = valor  # Asigna el valor al atributo valor
        self.hijos = {}  # Inicializa un diccionario vacío para almacenar los hijos del nodo

# Función para calcular la entropía de un conjunto de datos
def calcular_entropia(data):  # Define una función llamada calcular_entropia que toma un conjunto de datos como entrada
    etiquetas = {}  # Inicializa un diccionario vacío para contar las etiquetas únicas en el conjunto de datos
    for item in data:  # Itera sobre cada elemento (instancia) en el conjunto de datos
        etiqueta = item[-1]  # Obtiene la etiqueta del elemento
        if etiqueta not in etiquetas:  # Verifica si la etiqueta no está en el diccionario
            etiquetas[etiqueta] = 0  # Agrega la etiqueta al diccionario y establece su conteo en cero
        etiquetas[etiqueta] += 1  # Incrementa el conteo de la etiqueta en uno

    entropia = 0.0  # Inicializa la entropía en cero
    for etiqueta in etiquetas:  # Itera sobre cada etiqueta en el diccionario de etiquetas
        probabilidad = etiquetas[etiqueta] / len(data)  # Calcula la probabilidad de la etiqueta
        entropia -= probabilidad * math.log2(probabilidad)  # Calcula la contribución de esta etiqueta a la entropía total

    return entropia  # Retorna la entropía calculada

# Función para dividir el conjunto de datos en subconjuntos basados en un atributo dado
def dividir_data(data, atributo_idx):  # Define una función llamada dividir_data que toma un conjunto de datos y un índice de atributo como entrada
    data_dividida = {}  # Inicializa un diccionario vacío para almacenar los subconjuntos de datos divididos por los valores del atributo
    for item in data:  # Itera sobre cada elemento (instancia) en el conjunto de datos
        atributo_valor = item[atributo_idx]  # Obtiene el valor del atributo en el índice dado
        if atributo_valor not in data_dividida:  # Verifica si el valor del atributo no está en el diccionario
            data_dividida[atributo_valor] = []  # Agrega el valor del atributo al diccionario y establece su lista de elementos en vacío
        data_dividida[atributo_valor].append(item)  # Agrega el elemento al subconjunto correspondiente basado en el valor del atributo
    return data_dividida  # Retorna el diccionario de datos divididos

# Función para encontrar el atributo con la mayor ganancia de información
def encontrar_mejor_atributo(data, atributos):  # Define una función llamada encontrar_mejor_atributo que toma un conjunto de datos y una lista de atributos como entrada
    entropia_inicial = calcular_entropia(data)  # Calcula la entropía inicial del conjunto de datos
    mejor_ganancia_info = 0.0  # Inicializa la mejor ganancia de información en cero
    mejor_atributo = None  # Inicializa el mejor atributo como None
    for i in range(len(atributos)):  # Itera sobre cada índice de atributo en la lista de atributos
        atributo_valores = set([item[i] for item in data])  # Obtiene los valores únicos del atributo en el índice dado
        entropia_nueva = 0.0  # Inicializa la entropía después de dividir por este atributo en cero
        for valor in atributo_valores:  # Itera sobre cada valor del atributo
            data_dividida = dividir_data(data, i)  # Divide el conjunto de datos por el valor del atributo
            probabilidad = len(data_dividida[valor]) / len(data)  # Calcula la probabilidad de este valor del atributo
            entropia_nueva += probabilidad * calcular_entropia(data_dividida[valor])  # Calcula la entropía después de dividir por este valor del atributo
        ganancia_info = entropia_inicial - entropia_nueva  # Calcula la ganancia de información al dividir por este atributo
        if ganancia_info > mejor_ganancia_info:  # Verifica si la ganancia de información es mayor que la mejor ganancia de información encontrada hasta ahora
            mejor_ganancia_info = ganancia_info  # Actualiza la mejor ganancia de información
            mejor_atributo = i  # Actualiza el mejor atributo con este índice
    return mejor_atributo  # Retorna el índice del mejor atributo encontrado

# Función para construir el árbol de decisión usando el algoritmo ID3
def construir_arbol_decision(data, atributos, etiquetas):  # Define una función llamada construir_arbol_decision que toma un conjunto de datos, una lista de atributos y una lista de etiquetas como entrada
    # Caso base: si todos los ejemplos tienen la misma etiqueta, devolver un nodo hoja con esa etiqueta
    etiquetas_data = [item[-1] for item in data]  # Obtiene las etiquetas de los ejemplos
    if len(set(etiquetas_data)) == 1:  # Verifica si todas las etiquetas son iguales
        return Nodo(etiquetas_data[0])  # Retorna un nodo hoja con la etiqueta única encontrada

    # Si no quedan atributos, devolver un nodo hoja con la etiqueta más común
    if len(atributos) == 0:  # Verifica si no quedan atributos para dividir
        etiqueta_mas_comun = max(set(etiquetas_data), key=etiquetas_data.count)  # Encuentra la etiqueta más común en los ejemplos
        return Nodo(etiqueta_mas_comun)  # Retorna un nodo hoja con la etiqueta más común encontrada

    # Encontrar el mejor atributo para dividir
    mejor_atributo_idx = encontrar_mejor_atributo(data, atributos)  # Encuentra el índice del mejor atributo para dividir
    mejor_atributo = atributos[mejor_atributo_idx]  # Obtiene el nombre del mejor atributo

    # Construir el árbol recursivamente
    nodo = Nodo(mejor_atributo)  # Crea un nodo con el mejor atributo como valor
    atributos_restantes = atributos[:mejor_atributo_idx] + atributos[mejor_atributo_idx+1:]  # Elimina el mejor atributo de la lista de atributos restantes
    atributo_valores = set([item[mejor_atributo_idx] for item in data])  # Obtiene los valores únicos del mejor atributo
    for valor in atributo_valores:  # Itera sobre cada valor del mejor atributo
        data_dividida = [item for item in data if item[mejor_atributo_idx] == valor]  # Divide el conjunto de datos por este valor del mejor atributo
        nodo.hijos[valor] = construir_arbol_decision(data_dividida, atributos_restantes, etiquetas)  # Construye el subárbol recursivamente

    return nodo  # Retorna el nodo raíz del árbol de decisión construido

# Función para predecir la etiqueta de un ejemplo utilizando el árbol de decisión construido
def predecir_ejemplo(ejemplo, arbol_decision):  # Define una función llamada predecir_ejemplo que toma un ejemplo y el árbol de decisión construido como entrada
    if arbol_decision.valor in ejemplo:  # Verifica si el valor del nodo actual está presente en el ejemplo
        valor_atributo = ejemplo[arbol_decision.valor]  # Obtiene el valor del atributo del ejemplo
        if valor_atributo in arbol_decision.hijos:  # Verifica si el valor del atributo tiene un hijo en el árbol de decisión
            return predecir_ejemplo(ejemplo, arbol_decision.hijos[valor_atributo])  # Realiza una llamada recursiva con el hijo correspondiente
    return arbol_decision.valor  # Retorna el valor del nodo actual si no hay hijos correspondientes

# Datos de entrenamiento
atributos = ["pelo", "patas", "oviparo"]  # Lista de nombres de atributos
etiquetas = ["mamifero", "no mamifero"]  # Lista de etiquetas de clasificación
data_entrenamiento = [  # Lista de ejemplos de entrenamiento con sus atributos y etiquetas
    [True, 4, False, "mamifero"],
    [True, 4, False, "mamifero"],
    [False, 2, True, "no mamifero"],
    [False, 0, False, "mamifero"],
    [True, 4, False, "mamifero"],
    [False, 4, True, "no mamifero"]
]

# Construir el árbol de decisión
arbol_decision = construir_arbol_decision(data_entrenamiento, atributos, etiquetas)

# Ejemplos de prueba
ejemplo1 = {"pelo": True, "patas": 2, "oviparo": True}  # Ejemplo 1 con sus atributos
ejemplo2 = {"pelo": True, "patas": 4, "oviparo": False}  # Ejemplo 2 con sus atributos

# Predecir la etiqueta de los ejemplos de prueba
print("Ejemplo 1 - Es mamífero?" + ": " + predecir_ejemplo(ejemplo1, arbol_decision))  # Predice la etiqueta del Ejemplo 1
print("Ejemplo 2 - Es mamífero?" + ": " + predecir_ejemplo(ejemplo2, arbol_decision))  # Predice la etiqueta del Ejemplo 2
