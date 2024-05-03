##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random# Importación del módulo random para generar números aleatorios

def funcion_objetivo(posicion):# Función objetivo (puedes reemplazarla por tu propia función)
    # Supongamos una función de ejemplo que evalúa la posición en un tablero de ajedrez
    evaluacion = {
        ('a', '1'): 0.0, ('b', '1'): 0.1, ('c', '1'): 0.2, ('d', '1'): 0.3, ('e', '1'): 0.4,
        ('a', '2'): 0.1, ('b', '2'): 0.2, ('c', '2'): 0.3, ('d', '2'): 0.4, ('e', '2'): 0.5,
        ('a', '3'): 0.2, ('b', '3'): 0.3, ('c', '3'): 0.4, ('d', '3'): 0.5, ('e', '3'): 0.6,
        ('a', '4'): 0.3, ('b', '4'): 0.4, ('c', '4'): 0.5, ('d', '4'): 0.6, ('e', '4'): 0.7,
        ('a', '5'): 0.4, ('b', '5'): 0.5, ('c', '5'): 0.6, ('d', '5'): 0.7, ('e', '5'): 0.8,
    }
    return evaluacion.get(posicion, 0.0)  # Devuelve la evaluación de la posición o 0.0 si la posición no existe

# Función de ascenso de colinas con objetivo
def ascenso_colinas_con_objetivo(max_iter, rango_filas, rango_columnas):
    mejor_posicion = None  # Almacenará la mejor posición encontrada
    mejor_valor = float('-inf')  # Almacenará el mejor valor encontrado

    # Realizar el ascenso de colinas durante el número máximo de iteraciones especificado
    for _ in range(max_iter):
        # Seleccionar una posición aleatoria dentro del rango especificado
        fila = random.choice(rango_filas)
        columna = random.choice(rango_columnas)
        posicion_actual = (fila, columna)

        # Evaluar la función objetivo en la posición actual
        valor_actual = funcion_objetivo(posicion_actual)

        # Actualizar si encontramos una mejor posición
        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_posicion = posicion_actual

    return mejor_posicion, mejor_valor  # Devuelve la mejor posición y su valor

# Definir el rango de filas y columnas del tablero
rango_filas = ['a', 'b', 'c', 'd', 'e']
rango_columnas = ['1', '2', '3', '4', '5']

# Ejemplo de uso
max_iter = 1000  # Número máximo de iteraciones
# Realizar la búsqueda del ascenso de colinas con el número máximo de iteraciones y los rangos especificados
mejor_posicion, mejor_valor = ascenso_colinas_con_objetivo(max_iter, rango_filas, rango_columnas)

# Imprimir el resultado
print(f"La mejor posición encontrada es {mejor_posicion} con un valor de {mejor_valor}.")
