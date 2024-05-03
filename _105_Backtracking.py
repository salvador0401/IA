##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definimos una función para resolver el Sudoku utilizando backtracking
def solucionar_sudoku(sudoku):
    # Si no hay celdas vacías, el Sudoku está resuelto
    if not encontrar_celda_vacia(sudoku):
        return True

    # Encontramos la primera celda vacía
    fila, columna = encontrar_celda_vacia(sudoku)

    # Probamos números del 1 al 9 en la celda vacía
    for numero in range(1, 10):
        if es_numero_valido(sudoku, fila, columna, numero):
            sudoku[fila][columna] = numero

            # Llamamos recursivamente a la función para resolver el Sudoku
            if solucionar_sudoku(sudoku):
                return True

            # Si la recursión no encontró una solución, retrocedemos y probamos otro número
            sudoku[fila][columna] = 0

    # Si ningún número es válido para esta celda, indicamos que no hay solución
    return False

# Función para encontrar la primera celda vacía en el Sudoku
def encontrar_celda_vacia(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None

# Función para verificar si un número es válido para una celda específica
def es_numero_valido(sudoku, fila, columna, numero):
    return not en_fila(sudoku, fila, numero) and \
           not en_columna(sudoku, columna, numero) and \
           not en_cuadrante(sudoku, fila - fila % 3, columna - columna % 3, numero)

# Funciones auxiliares para verificar si un número está en una fila, columna o cuadrante
def en_fila(sudoku, fila, numero):
    return numero in sudoku[fila]

def en_columna(sudoku, columna, numero):
    return numero in [sudoku[i][columna] for i in range(9)]

def en_cuadrante(sudoku, fila_inicio, columna_inicio, numero):
    return any(numero == sudoku[fila][columna] for fila in range(fila_inicio, fila_inicio + 3) for columna in range(columna_inicio, columna_inicio + 3))

# Función para imprimir el Sudoku
def imprimir_sudoku(sudoku):
    for fila in sudoku:
        print(fila)

# Sudoku para resolver (0 representa una celda vacía)
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Imprimimos el problema de Sudoku
print("Problema de Sudoku:")
imprimir_sudoku(sudoku)

# Intentamos resolver el Sudoku
if solucionar_sudoku(sudoku):
    print("\nSolución encontrada:")
    imprimir_sudoku(sudoku)
else:
    print("\nNo se encontró solución.")
