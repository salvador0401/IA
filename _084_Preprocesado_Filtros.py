##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import cv2
import numpy as np 

img = cv2.imread('_084_Preprocesado_Filtros_imagen.jpg') 
img = cv2.resize(img, (300,250))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Imagen Original', img)

a_low = np.array([20,50,50], np.uint8)
a_high = np.array([32,255,255], np.uint8)
mascara2 = cv2.inRange(img2,a_low,a_high)

cv2.imshow ('Amarillo',mascara2)

cv2.waitKey(0) 
cv2.destroyAllWindows()
