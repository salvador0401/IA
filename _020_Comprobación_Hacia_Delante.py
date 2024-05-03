##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Restriccion:
    def __init__(self, variable1, variable2):
        # Inicializa una restricción entre dos variables.
        self.variable1 = variable1  # Variable 1 de la restricción.
        self.variable2 = variable2  # Variable 2 de la restricción.

    def cumple_restriccion(self, valor1, valor2):
        # Comprueba si dos valores cumplen la restricción (no pueden ser iguales).
        return valor1 != valor2  # Devuelve True si los valores son diferentes, False en caso contrario.


class CSP:
    def __init__(self, variables, dominio):
        # Inicializa una instancia de CSP con un conjunto de variables y su dominio.
        self.variables = variables  # Lista de variables del problema CSP.
        self.dominio = dominio  # Diccionario que asigna a cada variable su conjunto de valores posibles.
        self.restricciones = []  # Lista para almacenar las restricciones del problema.

    def agregar_restriccion(self, restriccion):
        # Agrega una restricción al problema CSP.
        self.restricciones.append(restriccion)  # Añade la restricción a la lista de restricciones.

    def comprobacion_hacia_adelante(self, variable, valor):
        # Realiza comprobación hacia adelante para propagar las restricciones cuando se asigna un valor a una variable.
        for restriccion in self.restricciones:
            # Itera sobre todas las restricciones del problema.
            if restriccion.variable1 == variable:
                # Si la primera variable de la restricción es la variable actual:
                vecino = restriccion.variable2  # Identifica la variable vecina.
                for val in self.dominio[vecino]:
                    # Itera sobre los valores del dominio de la variable vecina.
                    if not restriccion.cumple_restriccion(valor, val):
                        # Si el valor asignado y el valor de la variable vecina no cumplen la restricción:
                        self.dominio[vecino].remove(val)
                        # Elimina el valor de la lista de valores posibles de la variable vecina.


# Definimos las variables y su dominio (los colores disponibles)
variables = {'A', 'B', 'C', 'D'}  # Conjunto de variables del problema CSP.
dominio = {'A': ['rojo', 'verde', 'azul'],  # Diccionario que asigna a cada variable su conjunto de valores posibles.
           'B': ['rojo', 'verde', 'azul'],
           'C': ['rojo', 'verde', 'azul'],
           'D': ['rojo', 'verde', 'azul']}

# Creamos un CSP (Problema de Satisfacción de Restricciones)
csp = CSP(variables, dominio)  # Instanciamos un objeto CSP con las variables y el dominio definidos.

# Agregamos las restricciones (las regiones adyacentes no pueden tener el mismo color)
csp.agregar_restriccion(Restriccion('A', 'B'))  # Agregamos una restricción entre las variables 'A' y 'B'.
csp.agregar_restriccion(Restriccion('A', 'C'))  # Agregamos una restricción entre las variables 'A' y 'C'.
csp.agregar_restriccion(Restriccion('B', 'C'))  # Agregamos una restricción entre las variables 'B' y 'C'.
csp.agregar_restriccion(Restriccion('B', 'D'))  # Agregamos una restricción entre las variables 'B' y 'D'.
csp.agregar_restriccion(Restriccion('C', 'D'))  # Agregamos una restricción entre las variables 'C' y 'D'.

# Supongamos que asignamos un color a la región A
variable = 'A'  # Seleccionamos la variable 'A'.
valor = 'rojo'  # Asignamos el valor 'rojo' a la variable 'A'.

# Aplicamos comprobación hacia adelante para propagar las restricciones
csp.comprobacion_hacia_adelante(variable, valor)  # Realizamos la propagación de restricciones.

# Mostramos el dominio actualizado después de la propagación
print("Dominio después de la comprobación hacia adelante:")
for variable, valores in csp.dominio.items():
    # Iteramos sobre todas las variables y sus valores posibles en el dominio actualizado.
    print(variable + ":", valores)  # Imprimimos la variable y sus valores posibles después de la propagación.
