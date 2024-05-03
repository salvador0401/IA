##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class ConjuntoDifuso:
    def __init__(self, nombre, funcion_membresia):
        self.nombre = nombre  # Nombre del conjunto difuso
        self.funcion_membresia = funcion_membresia  # Función de membresía del conjunto difuso

    def membresia(self, valor):
        return self.funcion_membresia(valor)  # Calcula la membresía de un valor en el conjunto difuso


# Definir funciones de membresía para conjuntos difusos
def triangulo(a, b, c):
    def funcion(valor):
        if valor <= a or valor >= c:  # Si el valor está fuera del rango del triángulo
            return 0
        elif a < valor < b:  # Si el valor está dentro de la pendiente ascendente del triángulo
            return (valor - a) / (b - a)  # Calcula la membresía basado en la pendiente ascendente
        elif b <= valor <= c:  # Si el valor está dentro de la pendiente descendente del triángulo
            return (c - valor) / (c - b)  # Calcula la membresía basado en la pendiente descendente
        else:
            return 0  # Si el valor está fuera del rango del triángulo
    return funcion


def trapezoide(a, b, c, d):
    def funcion(valor):
        if valor <= a or valor >= d:  # Si el valor está fuera del rango del trapezoide
            return 0
        elif a < valor < b:  # Si el valor está dentro de la pendiente ascendente del trapezoide
            return (valor - a) / (b - a)  # Calcula la membresía basado en la pendiente ascendente
        elif c < valor < d:  # Si el valor está dentro de la pendiente descendente del trapezoide
            return (d - valor) / (d - c)  # Calcula la membresía basado en la pendiente descendente
        else:
            return 1  # Si el valor está dentro del rango horizontal del trapezoide
    return funcion


# Crear conjuntos difusos
conjunto_frio = ConjuntoDifuso("Frio", trapezoide(0, 0, 10, 20))  # Crear un conjunto difuso llamado "Frio" con una función de membresía trapezoidal
conjunto_caliente = ConjuntoDifuso("Caliente", trapezoide(10, 20, 30, 30))  # Crear un conjunto difuso llamado "Caliente" con una función de membresía trapezoidal

# Calcular membresía de un valor en cada conjunto difuso
temperatura = 15
print(f"La membresía de {temperatura} en el conjunto {conjunto_frio.nombre} es: {conjunto_frio.membresia(temperatura)}")  # Calcular la membresía del valor de temperatura en el conjunto "Frio"
print(f"La membresía de {temperatura} en el conjunto {conjunto_caliente.nombre} es: {conjunto_caliente.membresia(temperatura)}")  # Calcular la membresía del valor de temperatura en el conjunto "Caliente"
