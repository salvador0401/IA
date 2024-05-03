##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class FuncionUtilidadLineal:  # Define una clase llamada FuncionUtilidadLineal
    def __init__(self, pendiente, interseccion):  # Define el método de inicialización con pendiente e intersección
        self.pendiente = pendiente  # Asigna el valor de pendiente al atributo pendiente de la instancia
        self.interseccion = interseccion  # Asigna el valor de intersección al atributo interseccion de la instancia

    def calcular_utilidad(self, cantidad):  # Define un método para calcular la utilidad
        return self.pendiente * cantidad + self.interseccion  # Calcula la utilidad lineal

def tomar_decision(funcion_utilidad, opciones):  # Define una función para tomar decisiones
    mejor_opcion = None  # Inicializa la mejor opción como nula
    mejor_utilidad = float('-inf')  # Inicializa la mejor utilidad como negativa infinita
    for opcion, cantidad in opciones.items():  # Itera sobre las opciones y cantidades proporcionadas
        utilidad_opcion = funcion_utilidad.calcular_utilidad(cantidad)  # Calcula la utilidad de la opción actual
        if utilidad_opcion > mejor_utilidad:  # Comprueba si la utilidad actual es mejor que la mejor utilidad encontrada hasta ahora
            mejor_opcion = opcion  # Actualiza la mejor opción
            mejor_utilidad = utilidad_opcion  # Actualiza la mejor utilidad
    return mejor_opcion  # Devuelve la mejor opción encontrada

# Ejemplo de uso:
if __name__ == "__main__":  # Comprueba si el script se está ejecutando directamente
    funcion_utilidad = FuncionUtilidadLineal(pendiente=0.5, interseccion=0)  # Creamos una función de utilidad lineal
    opciones = {"Opción A": 10, "Opción B": 20, "Opción C": 15}  # Definimos las opciones y sus cantidades asociadas
    mejor_opcion = tomar_decision(funcion_utilidad, opciones)  # Tomamos la decisión basada en la función de utilidad
    print("La mejor opción es:", mejor_opcion)  # Imprime la mejor opción encontrada
