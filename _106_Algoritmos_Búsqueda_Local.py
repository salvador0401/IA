##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random

# Función para generar un tablero inicial
def generar_tablero(n):
    tablero = []
    columnas_disponibles = list(range(n))  # Lista de columnas disponibles
    for _ in range(n):
        columna = random.choice(columnas_disponibles)  # Se elige una columna disponible aleatoriamente
        fila = [0] * n  # Se crea una fila con todas las celdas inicializadas a 0
        fila[columna] = 1  # Se coloca una reina en la columna elegida
        tablero.append(fila)  # Se agrega la fila al tablero
        columnas_disponibles.remove(columna)  # Se elimina la columna elegida de las disponibles
    return tablero

# Función para evaluar un tablero (número de ataques entre reinas)
def evaluar_tablero(tablero):
    n = len(tablero)
    ataques = 0
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 1:
                for k in range(n):
                    if k != i:
                        # Verificar ataques en la misma fila
                        if tablero[k][j] == 1:
                            ataques += 1
                        # Verificar ataques en la misma diagonal
                        if abs(k - i) == abs(tablero[k].index(1) - j):
                            ataques += 1
    return ataques // 2  # Dividido por 2 ya que cada ataque se cuenta dos veces

# Función para mover una reina a una nueva columna
def mover_reina(tablero, fila, nueva_columna):
    tablero[fila] = [0] * len(tablero)  # Se reinicia la fila a 0
    tablero[fila][nueva_columna] = 1  # Se coloca la reina en la nueva columna

# Algoritmo de búsqueda local
def busqueda_local(n, iteraciones):
    mejor_tablero = generar_tablero(n)  # Se genera un tablero inicial
    mejor_evaluacion = evaluar_tablero(mejor_tablero)  # Se evalúa el tablero inicial

    for _ in range(iteraciones):
        fila = random.randint(0, n - 1)  # Se elige una fila aleatoria
        columna_actual = mejor_tablero[fila].index(1)  # Se encuentra la columna actual de la reina en esa fila
        nueva_columna = random.randint(0, n - 1)  # Se elige una nueva columna aleatoria
        if nueva_columna != columna_actual:
            tablero_temporal = [fila[:] for fila in mejor_tablero]  # Se crea una copia temporal del tablero
            mover_reina(tablero_temporal, fila, nueva_columna)  # Se mueve la reina a la nueva columna
            evaluacion_temporal = evaluar_tablero(tablero_temporal)  # Se evalúa el tablero temporal
            if evaluacion_temporal < mejor_evaluacion:
                mejor_tablero = tablero_temporal  # Se actualiza el mejor tablero si la evaluación es mejor
                mejor_evaluacion = evaluacion_temporal
        if mejor_evaluacion == 0:
            break

    return mejor_tablero

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("Q" if celda == 1 else "." for celda in fila))

# Parámetros del problema
n = 8  # Número de reinas y tamaño del tablero de ajedrez
iteraciones = 10000  # Número máximo de iteraciones del algoritmo de búsqueda local

# Resolución del problema
mejor_tablero = busqueda_local(n, iteraciones)  # Se busca la mejor solución

# Verificación adicional
def verificar_solucion(tablero):
    for i in range(n):
        for j in range(i+1, n):
            # Verificar filas y columnas
            if sum(tablero[i]) > 1 or sum(tablero[j]) > 1 or tablero[i].index(1) == tablero[j].index(1):
                return False
            # Verificar diagonales
            if abs(i - j) == abs(tablero[i].index(1) - tablero[j].index(1)):
                return False
    return True

# Se imprime la solución si es válida
if verificar_solucion(mejor_tablero):
    print("Solución válida:")
    imprimir_tablero(mejor_tablero)
else:
    print("Solución inválida.")
