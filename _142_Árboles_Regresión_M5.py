##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la biblioteca NumPy para operaciones numéricas
    
# Definición de la clase Nodo para el árbol de regresión
class Nodo:  # Define una clase llamada Nodo
    def __init__(self, atributo=None, umbral=None, valor=None, hijos=None):  # Define el método de inicialización de la clase Nodo con atributos opcionales
        self.atributo = atributo  # Atributo utilizado para dividir el nodo
        self.umbral = umbral      # Umbral utilizado para dividir el nodo
        self.valor = valor        # Valor de regresión para el nodo
        self.hijos = hijos        # Lista de nodos hijos

# Función para calcular el error cuadrático medio
def calcular_error_cuadratico_medio(y_true, y_pred):  # Define una función llamada calcular_error_cuadratico_medio que toma dos arrays de valores reales como entrada
    return np.mean((y_true - y_pred) ** 2)  # Calcula y retorna el error cuadrático medio entre los valores reales y predichos

# Función para dividir los datos en función de un atributo y umbral dados
def dividir_datos(X, y, atributo, umbral):  # Define una función llamada dividir_datos que toma un conjunto de datos X, un vector de etiquetas y, un índice de atributo y un umbral como entrada
    izquierda = np.where(X[:, atributo] <= umbral)  # Obtiene los índices de las filas donde el valor del atributo es menor o igual al umbral
    derecha = np.where(X[:, atributo] > umbral)  # Obtiene los índices de las filas donde el valor del atributo es mayor al umbral
    return izquierda, derecha  # Retorna los índices de las filas para las divisiones izquierda y derecha

# Función para ajustar un modelo de regresión lineal a los datos
def ajustar_modelo_regresion(X, y):  # Define una función llamada ajustar_modelo_regresion que toma un conjunto de datos X y un vector de etiquetas y como entrada
    return np.linalg.lstsq(X, y, rcond=None)[0]  # Ajusta un modelo de regresión lineal a los datos y retorna los coeficientes del modelo

# Función para construir el árbol de regresión utilizando el algoritmo M5
def construir_arbol_regresion(X, y, max_profundidad, min_muestras_split):  # Define una función llamada construir_arbol_regresion que toma un conjunto de datos X, un vector de etiquetas y, la profundidad máxima del árbol y el número mínimo de muestras para dividir un nodo como entrada
    if max_profundidad == 0 or len(X) < min_muestras_split:  # Verifica si se alcanzó la profundidad máxima o si hay muy pocas muestras para dividir
        return Nodo(valor=np.mean(y))  # Retorna un nodo hoja con el valor medio de las etiquetas

    mejor_atributo = None  # Inicializa el mejor atributo para dividir en None
    mejor_umbral = None  # Inicializa el mejor umbral para dividir en None
    mejor_error = np.inf  # Inicializa el mejor error como infinito
    mejor_izquierda = None  # Inicializa los índices de la división izquierda como None
    mejor_derecha = None  # Inicializa los índices de la división derecha como None

    for atributo in range(X.shape[1]):  # Itera sobre cada atributo
        for umbral in np.unique(X[:, atributo]):  # Itera sobre cada umbral único del atributo
            izquierda, derecha = dividir_datos(X, y, atributo, umbral)  # Divide los datos en función del atributo y el umbral

            if len(izquierda[0]) < min_muestras_split or len(derecha[0]) < min_muestras_split:  # Verifica si hay suficientes muestras en ambos lados para dividir
                continue  # Si no, pasa al siguiente umbral

            y_izquierda = y[izquierda]  # Etiquetas correspondientes a la división izquierda
            y_derecha = y[derecha]  # Etiquetas correspondientes a la división derecha

            modelo_izquierda = ajustar_modelo_regresion(X[izquierda], y_izquierda)  # Ajusta un modelo de regresión lineal a los datos de la división izquierda
            modelo_derecha = ajustar_modelo_regresion(X[derecha], y_derecha)  # Ajusta un modelo de regresión lineal a los datos de la división derecha

            y_pred_izquierda = np.dot(X[izquierda], modelo_izquierda)  # Predicciones de la división izquierda
            y_pred_derecha = np.dot(X[derecha], modelo_derecha)  # Predicciones de la división derecha

            error = calcular_error_cuadratico_medio(y[izquierda], y_pred_izquierda) + calcular_error_cuadratico_medio(y[derecha], y_pred_derecha) # Calcula el error cuadrático medio total para la división actual
            if error < mejor_error:  # Verifica si el error es menor que el mejor error hasta ahora
                mejor_atributo = atributo  # Actualiza el mejor atributo y umbral
                mejor_umbral = umbral
                mejor_error = error  # Actualiza el mejor error
                mejor_izquierda = izquierda  # Actualiza los índices de la división izquierda
                mejor_derecha = derecha  # Actualiza los índices de la división derecha

    if mejor_error == np.inf:  # Si no se encontró un umbral válido para dividir
        return Nodo(valor=np.mean(y))  # Retorna un nodo hoja con el valor medio de las etiquetas

    nodo_izquierda = construir_arbol_regresion(X[mejor_izquierda], y[mejor_izquierda], max_profundidad - 1, min_muestras_split)  # Construye recursivamente el subárbol izquierdo
    nodo_derecha = construir_arbol_regresion(X[mejor_derecha], y[mejor_derecha], max_profundidad - 1, min_muestras_split)  # Construye recursivamente el subárbol derecho

    return Nodo(atributo=mejor_atributo, umbral=mejor_umbral, hijos=[nodo_izquierda, nodo_derecha])  # Retorna un nodo interno con el mejor atributo y umbral, y sus nodos hijos

# Función para predecir el valor de regresión de un ejemplo utilizando el árbol de regresión construido
def predecir_valor_regresion(ejemplo, arbol):  # Define una función llamada predecir_valor_regresion que toma un ejemplo y el árbol de regresión como entrada
    if arbol.valor is not None:  # Si el nodo actual es una hoja, retorna su valor de regresión
        return arbol.valor

    if ejemplo[arbol.atributo] <= arbol.umbral:  # Si el valor del ejemplo en el atributo del nodo es menor o igual al umbral, sigue por el hijo izquierdo
        return predecir_valor_regresion(ejemplo, arbol.hijos[0])
    else:  # Si es mayor, sigue por el hijo derecho
        return predecir_valor_regresion(ejemplo, arbol.hijos[1])

# Ejemplo de datos de entrada
X = np.array([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])  # Datos de entrada
y = np.array([1, 2, 3, 4, 5])  # Etiquetas de salida

# Construir el árbol de regresión
arbol_regresion = construir_arbol_regresion(X, y, max_profundidad=2, min_muestras_split=2)

# Ejemplo de predicción
ejemplo = [1, 3]  # Ejemplo a predecir
valor_predicho = predecir_valor_regresion(ejemplo, arbol_regresion)  # Predice el valor de regresión para el ejemplo dado
print("Valor predicho para el ejemplo {}: {}".format(ejemplo, valor_predicho))  # Imprime el valor predicho
