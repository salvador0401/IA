##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Importa la librería OpenCV para procesamiento de imágenes
import cv2  
# Importa la librería NumPy para operaciones numéricas
import numpy as np  

# Lee la imagen desde el archivo "_084_Preprocesado_Filtros_imagen.jpg"
img = cv2.imread('_084_Preprocesado_Filtros_imagen.jpg') 
# Cambia el tamaño de la imagen a 300x250 píxeles
img = cv2.resize(img, (300,250))

# Convierte la imagen de formato BGR a HSV
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Muestra la imagen original en una ventana llamada "Imagen Original"
cv2.imshow('Imagen Original', img)

# Define el rango de colores del fondo en el espacio de color HSV
fondo_bajo = np.array([100, 100, 100], np.uint8)
fondo_alto = np.array([140, 255, 255], np.uint8)

# Define el rango de colores para seleccionar todos los píxeles excepto el fondo
todos_low = np.array([0, 100, 100], np.uint8)
todos_high = np.array([255, 255, 255], np.uint8)

# Crea una máscara para el fondo utilizando la función inRange de OpenCV
mascara_fondo = cv2.inRange(img2, fondo_bajo, fondo_alto)
# Crea una máscara para seleccionar todos los píxeles excepto el fondo
mascara_todos= cv2.bitwise_not(mascara_fondo)
# Aplica la máscara a la imagen HSV para eliminar el fondo
mascara = cv2.bitwise_and(img2,img2,mask=mascara_todos)

# Muestra la imagen resultante con los píxeles del fondo eliminados en una ventana llamada "Todo"
cv2.imshow ('Todo',mascara)
cv2.waitKey(0)  # Espera hasta que se presione una tecla
cv2.destroyAllWindows()  # Cierra todas las ventanas mostradas

