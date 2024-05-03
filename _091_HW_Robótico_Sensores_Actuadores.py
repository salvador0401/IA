##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import time  # Importa el módulo time para pausas
import random  # Importa el módulo random para generar valores aleatorios

# Clase del sensor de distancia ficticio
class SensorDistancia:
    def __init__(self):  # Método constructor de la clase
        pass  # No realiza ninguna acción

    def leer_distancia(self):  # Método para simular la lectura de distancia
        # Simular lectura de distancia
        return random.randint(0, 100)  # Devuelve un valor aleatorio entre 0 y 100 (cm)

# Clase del actuador de motor ficticio
class Motor:
    def __init__(self):  # Método constructor de la clase
        pass  # No realiza ninguna acción

    def mover(self, direccion):  # Método para simular el movimiento del motor
        # Simular movimiento del motor
        print(f'Moviendo motor en dirección {direccion}')  # Imprime la dirección del movimiento

# Función principal que simula el comportamiento del robot
def simular_robot(sensor, motor, movimientos=10):  # Define la función con los parámetros sensor, motor y movimientos (valor predeterminado: 10)
    movimientos_realizados = 0  # Inicializa el contador de movimientos realizados
    while movimientos_realizados < movimientos:  # Bucle while que se ejecuta mientras se hayan realizado menos movimientos que el total
        # Leer la distancia del sensor
        distancia = sensor.leer_distancia()  # Llama al método leer_distancia del sensor
        print(f'Distancia leída: {distancia} cm')  # Imprime la distancia leída

        # Tomar decisiones basadas en la distancia
        if distancia > 50:  # Si la distancia es mayor que 50 cm
            motor.mover('adelante')  # Llama al método mover del motor con la dirección 'adelante'
        else:  # Si la distancia es menor o igual a 50 cm
            motor.mover('atras')  # Llama al método mover del motor con la dirección 'atras'

        movimientos_realizados += 1  # Incrementa el contador de movimientos realizados

        time.sleep(1)  # Pausa el programa durante 1 segundo entre cada iteración

# Crear instancia del sensor y del motor
sensor = SensorDistancia()  # Crea una instancia de la clase SensorDistancia
motor = Motor()  # Crea una instancia de la clase Motor

# Simular comportamiento del robot con 10 movimientos
simular_robot(sensor, motor, movimientos=10)  # Llama a la función simular_robot con los objetos sensor y motor, y 10 movimientos como parámetro
