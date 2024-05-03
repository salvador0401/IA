##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np
# Importamos la librería NumPy para manipulación de matrices y arreglos multidimensionales.

# Función para detectar si una línea es horizontal o vertical
def detectar_linea(imagen):
    # Definimos una función llamada detectar_linea que toma una matriz imagen como entrada.
    
    altura, ancho = imagen.shape
    # Obtenemos las dimensiones de la imagen (altura y ancho) utilizando el método .shape de NumPy.

    # Calculamos la suma de los valores de píxeles a lo largo de las filas y columnas
    suma_filas = np.sum(imagen, axis=1)
    suma_columnas = np.sum(imagen, axis=0)
    # Calculamos la suma de los valores de píxeles a lo largo de las filas (axis=1) y columnas (axis=0).

    # Si la suma de píxeles a lo largo de las filas es mayor que la suma de las columnas,
    # la línea es probablemente horizontal; de lo contrario, es probablemente vertical.
    if np.mean(suma_filas) > np.mean(suma_columnas):
        return "horizontal"
    else:
        return "vertical"
    # Comparamos las medias de las sumas de píxeles de filas y columnas para determinar si la línea es horizontal o vertical.

# Ejemplo de imagen (matriz de píxeles)
imagen_horizontal = np.array([[0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]])
# Definimos una imagen de ejemplo que contiene una línea horizontal.

imagen_vertical = np.array([[0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0],
                            [0, 1, 0, 0, 0]])
# Definimos otra imagen de ejemplo que contiene una línea vertical.

# Probamos la función con ejemplos
resultado_horizontal = detectar_linea(imagen_horizontal)
resultado_vertical = detectar_linea(imagen_vertical)
# Llamamos a la función detectar_linea con las imágenes de ejemplo.

print("La línea en la imagen horizontal es:", resultado_horizontal)
print("La línea en la imagen vertical es:", resultado_vertical)
# Imprimimos los resultados de la detección de línea para las imágenes de ejemplo.
