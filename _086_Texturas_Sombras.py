##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import cv2  # Importa la librería OpenCV para procesamiento de imágenes
import numpy as np  # Importa la librería NumPy para operaciones numéricas

img = cv2.imread('_084_Preprocesado_Filtros_imagen.jpg')  # Lee la imagen desde el archivo "_084_Preprocesado_Filtros_imagen.jpg"
img = cv2.resize(img, (300,250))  # Cambia el tamaño de la imagen a 300x250 píxeles
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # Convierte la imagen de formato BGR a HSV
cv2.imshow('Imagen Original', img)  # Muestra la imagen original en una ventana llamada "Imagen Original"

cv2.imshow('Imagen HSV.png', img2)  # Muestra la imagen convertida a HSV en una ventana llamada "Imagen HSV.png"
cv2.waitKey(0)  # Espera hasta que se presione una tecla
cv2.destroyAllWindows()  # Cierra todas las ventanas mostradas
