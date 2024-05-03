##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Evento:  # Define una clase llamada Evento para representar un evento en la red de decisión
    def __init__(self, probabilidad, resultado_bueno, resultado_malo):  # Define el método de inicialización con probabilidad y resultados buenos y malos
        self.probabilidad = probabilidad  # Asigna la probabilidad del evento al atributo probabilidad de la instancia
        self.resultado_bueno = resultado_bueno  # Asigna el resultado bueno al atributo resultado_bueno de la instancia
        self.resultado_malo = resultado_malo  # Asigna el resultado malo al atributo resultado_malo de la instancia

class Decision:  # Define una clase llamada Decision para representar una decisión en la red de decisión
    def __init__(self, nombre):  # Define el método de inicialización con el nombre de la decisión
        self.nombre = nombre  # Asigna el nombre de la decisión al atributo nombre de la instancia

class Opcion:  # Define una clase llamada Opcion para representar una opción en la red de decisión
    def __init__(self, nombre, resultados):  # Define el método de inicialización con el nombre de la opción y sus resultados
        self.nombre = nombre  # Asigna el nombre de la opción al atributo nombre de la instancia
        self.resultados = resultados  # Asigna los resultados de la opción al atributo resultados de la instancia

def calcular_utilidad(opcion, evento_bueno, evento_malo):  # Define una función para calcular la utilidad esperada de una opción
    utilidad = opcion.resultados[0] * evento_bueno.probabilidad + opcion.resultados[1] * evento_malo.probabilidad  # Calcula la utilidad esperada
    return utilidad  # Devuelve la utilidad esperada de la opción

def tomar_decision(opcion_a, opcion_b, evento_bueno, evento_malo):  # Define una función para tomar una decisión entre dos opciones
    utilidad_opcion_a = calcular_utilidad(opcion_a, evento_bueno, evento_malo)  # Calcula la utilidad esperada de la opción A
    utilidad_opcion_b = calcular_utilidad(opcion_b, evento_bueno, evento_malo)  # Calcula la utilidad esperada de la opción B

    if utilidad_opcion_a > utilidad_opcion_b:  # Comprueba si la utilidad esperada de la opción A es mayor que la de la opción B
        return opcion_a.nombre  # Devuelve el nombre de la opción A como la mejor opción
    elif utilidad_opcion_b > utilidad_opcion_a:  # Comprueba si la utilidad esperada de la opción B es mayor que la de la opción A
        return opcion_b.nombre  # Devuelve el nombre de la opción B como la mejor opción
    else:  # Si las utilidades esperadas son iguales
        return "Ambas opciones tienen la misma utilidad esperada."  # Devuelve un mensaje indicando que ambas opciones son igualmente buenas

if __name__ == "__main__":  # Comprueba si el script se está ejecutando directamente
    # Definir eventos
    evento_bueno = Evento(probabilidad=0.8, resultado_bueno=100, resultado_malo=0)  # Crea un evento bueno con probabilidad 0.8 y resultados buenos y malos
    evento_malo = Evento(probabilidad=0.2, resultado_bueno=20, resultado_malo=0)  # Crea un evento malo con probabilidad 0.2 y resultados buenos y malos

    # Definir opciones
    opcion_a = Opcion(nombre="Opción A", resultados=(100, 0))  # Crea la opción A con nombre y resultados
    opcion_b = Opcion(nombre="Opción B", resultados=(50, 50))  # Crea la opción B con nombre y resultados

    # Tomar decisión
    decision = tomar_decision(opcion_a, opcion_b, evento_bueno, evento_malo)  # Llama a la función para tomar una decisión entre las opciones
    print("La mejor opción es:", decision)  # Imprime la mejor opción encontrada
