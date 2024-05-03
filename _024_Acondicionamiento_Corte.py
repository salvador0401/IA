##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Restriccion:
    def __init__(self, var1, var2, condicion):  # Define una restricción binaria con dos variables y una condición
        self.var1 = var1  # Almacena la primera variable de la restricción
        self.var2 = var2  # Almacena la segunda variable de la restricción
        self.condicion = condicion  # Almacena la función de condición que debe cumplirse
    
    def satisfecha(self, asignacion):  # Verifica si la restricción se satisface dado un conjunto de asignaciones
        if self.var1 not in asignacion or self.var2 not in asignacion:  # Si alguna variable no está asignada, la restricción se considera satisfecha
            return True
        return self.condicion(asignacion[self.var1], asignacion[self.var2])  # Evalúa la condición con las asignaciones de las variables

def no_igual(a, b):  # Define la función de condición "no igual"
    return a != b

def igual(a, b):  # Define la función de condición "igual"
    return a == b

class ProblemaSR:
    def __init__(self, variables, dominios):  # Define un problema de Satisfacción de Restricciones (SR) con variables y dominios
        self.variables = variables  # Almacena las variables del problema
        self.dominios = dominios  # Almacena los dominios de cada variable
        self.restricciones = {}  # Inicializa un diccionario para almacenar las restricciones
        for var in self.variables:  # Para cada variable del problema
            self.restricciones[var] = []  # Inicializa una lista vacía de restricciones
        
        # Verifica que cada variable tenga un dominio asignado
        for var in self.variables:
            if var not in self.dominios:
                raise LookupError("Cada variable debe tener un dominio asignado.")
    
    def agregar_restriccion(self, restriccion):  # Agrega una restricción al problema
        for var in restriccion.var1, restriccion.var2:  # Para cada variable en la restricción
            if var not in self.variables:  # Verifica que la variable esté en el conjunto de variables del problema
                raise LookupError("Variable en la restricción no está en el ProblemaSR.")
            self.restricciones[var].append(restriccion)  # Agrega la restricción a la lista de restricciones de la variable
    
    def consistente(self, variable, valor, asignacion):  # Verifica si una asignación es consistente con las restricciones
        for restriccion in self.restricciones[variable]:  # Para cada restricción asociada a la variable
            if not restriccion.satisfecha(asignacion):  # Si alguna restricción no se satisface con la asignación dada
                return False  # La asignación no es consistente
        return True  # Si todas las restricciones se satisfacen, la asignación es consistente
    
    def búsqueda_atrás(self, asignación={}):  # Implementa el algoritmo de búsqueda atrás para resolver el problema
        if len(asignación) == len(self.variables):  # Si todas las variables están asignadas
            return asignación  # Retorna la asignación como solución
        no_asignadas = [var for var in self.variables if var not in asignación]  # Obtiene las variables no asignadas
        primera = no_asignadas[0]  # Escoge la primera variable no asignada
        for valor in self.dominios[primera]:  # Para cada valor en el dominio de la primera variable no asignada
            if self.consistente(primera, valor, asignación):  # Si la asignación es consistente con las restricciones
                asignación[primera] = valor  # Asigna el valor a la variable
                resultado = self.búsqueda_atrás(asignación)  # Realiza una búsqueda recursiva con la nueva asignación
                if resultado is not None:  # Si se encuentra una solución
                    return resultado  # Retorna la solución encontrada
                del asignación[primera]  # Si no se encontró una solución, deshace la asignación
        return None  # Si no se encontró solución para la asignación actual, retorna None

# Ejemplo de uso:
variables = ['A', 'B', 'C']  # Definición de las variables del problema
dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}  # Definición de los dominios de las variables

problema = ProblemaSR(variables, dominios)  # Creación de una instancia del problema SR
problema.agregar_restriccion(Restriccion('A', 'B', no_igual))  # Agrega una restricción que A y B no pueden ser iguales
problema.agregar_restriccion(Restriccion('B', 'C', igual))  # Agrega una restricción que B y C deben ser iguales

solución = problema.búsqueda_atrás()  # Resuelve el problema utilizando búsqueda atrás
if solución:  # Si se encontró una solución
    print("Solución encontrada:")  # Imprime un mensaje indicando que se encontró una solución
    for variable, valor in solución.items():  # Para cada variable en la solución
        print(f"{variable}: {valor}")  # Imprime la variable y su valor
else:  # Si no se encontró una solución
    print("No se encontró solución para el problema.")  # Imprime un mensaje indicando que no se encontró solución
