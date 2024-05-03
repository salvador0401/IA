##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import easyocr
from PIL import Image

# Crear un objeto EasyOCR
reader = easyocr.Reader(['es'])

# Cargar la imagen
image = Image.open('imagen.jpg')

# Redimensionar la imagen (ajusta el tamaño según sea necesario)
width, height = image.size
if width > 1000 or height > 1000:
    image = image.resize((width // 2, height // 2))

# Realizar OCR en la imagen
result = reader.readtext(image)

# Iterar sobre los resultados y extraer el texto
for detection in result:
    text = detection[1]
    print('Texto detectado: "{}"'.format(text))

# Mostrar la imagen con el texto resaltado
image.show()
