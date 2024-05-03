##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Importar las bibliotecas necesarias
import speech_recognition as sr  # Biblioteca para el reconocimiento de voz
import pygame  # Biblioteca para la creación de gráficos por computadora
import sys  # Biblioteca para interactuar con el sistema operativo

# Inicializar Pygame
pygame.init()  # Inicializar Pygame
screen = pygame.display.set_mode((800, 600))  # Crear una ventana de 800x600 píxeles
pygame.display.set_caption('Speech Recognition Graphics')  # Establecer el título de la ventana

# Función para representar gráficamente un círculo
def draw_circle(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)  # Dibujar un círculo rojo en la posición especificada

# Función para representar gráficamente un cuadrado
def draw_square(x, y):
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x-50, y-50, 100, 100))  # Dibujar un cuadrado verde en la posición especificada

# Función principal
def main():
    recognizer = sr.Recognizer()  # Crear un objeto para el reconocimiento de voz
    command_recognized = False  # Bandera para indicar si se ha reconocido un comando

    running = True  # Bandera para indicar si el programa está en ejecución
    while running:  # Bucle principal del programa
        for event in pygame.event.get():  # Iterar sobre los eventos pygame
            if event.type == pygame.QUIT:  # Si se presiona el botón de cierre de la ventana
                running = False  # Establecer la bandera de ejecución en False
            elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if event.key == pygame.K_ESCAPE:  # Si la tecla presionada es 'Esc'
                    running = False  # Establecer la bandera de ejecución en False

        if not command_recognized:  # Si no se ha reconocido un comando
            with sr.Microphone() as source:  # Abrir el micrófono
                print("Diga un comando ('circular' o 'cuadrado'):")  # Solicitar al usuario que hable un comando
                audio = recognizer.listen(source)  # Escuchar el audio del micrófono

            try:  # Intentar reconocer el audio
                command = recognizer.recognize_google(audio)  # Reconocer el comando usando Google Speech Recognition
                print("Comando reconocido:", command)  # Imprimir el comando reconocido
                
                if "circular" in command:  # Si el comando es "círculo"
                    draw_circle(400, 300)  # Dibujar un círculo en la posición especificada
                elif "cuadrado" in command:  # Si el comando es "cuadrado"
                    draw_square(400, 300)  # Dibujar un cuadrado en la posición especificada
                else:  # Si el comando no es reconocido
                    print("Comando no reconocido")  # Imprimir un mensaje indicando que el comando no es reconocido
                
                pygame.display.flip()  # Actualizar la pantalla después de dibujar
                command_recognized = True  # Establecer la bandera de comando reconocido en True

            except sr.UnknownValueError:  # Si no se puede entender el audio
                print("No se pudo entender el audio")  # Imprimir un mensaje indicando que no se pudo entender el audio
            except sr.RequestError as e:  # Si hay un error en la solicitud
                print("Error al solicitar resultados; {0}".format(e))  # Imprimir el error de la solicitud

    pygame.quit()  # Cerrar Pygame
    sys.exit()  # Salir del programa

if __name__ == "__main__":  # Si este script es el programa principal
    main()  # Llamar a la función principal
