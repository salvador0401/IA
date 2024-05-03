##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de la clase CSP (Problema de Satisfacción de Restricciones)
class CSP:
    # Constructor de la clase
    def __init__(self, variables, dominios):
        # Inicialización de las variables y dominios
        self.variables = variables
        self.dominios = dominios
        self.restricciones = {}

    # Método para agregar una restricción al problema CSP
    def agregar_restriccion(self, restriccion):
        # Itera sobre las variables en el alcance de la restricción
        for var in restriccion.alcance:
            # Verifica si la variable no está en las restricciones
            if var not in self.restricciones:
                # Si no está, crea una lista vacía para esa variable
                self.restricciones[var] = []
            # Agrega la restricción a la lista de restricciones de la variable
            self.restricciones[var].append(restriccion)

    # Método para verificar si una asignación es consistente con las restricciones
    def consistente(self, var, valor, asignacion):
        # Itera sobre las restricciones asociadas a la variable
        for restriccion in self.restricciones.get(var, []):
            # Verifica si la restricción se satisface con el valor dado y la asignación actual
            if not restriccion.satisfecha(valor, asignacion):
                return False
        return True

    # Método para realizar la búsqueda por retroceso (backtracking)
    def busqueda_retroceso(self, asignacion={}):
        # Verifica si la asignación actual cubre todas las variables
        if len(asignacion) == len(self.variables):
            return asignacion
        # Selecciona una variable no asignada
        var = self.seleccionar_variable_no_asignada(asignacion)
        # Itera sobre los valores en el dominio de la variable
        for valor in self.ordenar_valores_dominio(var, asignacion):
            # Verifica si el valor es consistente con la asignación actual
            if self.consistente(var, valor, asignacion):
                # Asigna el valor a la variable
                asignacion[var] = valor
                # Realiza la búsqueda recursiva con la nueva asignación
                resultado = self.busqueda_retroceso(asignacion)
                # Si se encuentra una solución, la devuelve
                if resultado is not None:
                    return resultado
                # Si no se encuentra una solución, deshace la asignación
                del asignacion[var]
        # Si no se encuentra ninguna solución, devuelve None
        return None

    # Método para seleccionar una variable no asignada
    def seleccionar_variable_no_asignada(self, asignacion):
        # Itera sobre las variables y devuelve la primera no asignada
        for var in self.variables:
            if var not in asignacion:
                return var

    # Método para ordenar los valores del dominio de una variable
    def ordenar_valores_dominio(self, var, asignacion):
        # Devuelve los valores del dominio sin ordenar
        return self.dominios[var]


# Definición de la clase Restriccion (base para otras restricciones)
class Restriccion:
    # Constructor de la clase
    def __init__(self, alcance):
        # Inicialización del alcance de la restricción
        self.alcance = alcance

    # Método para verificar si la restricción se satisface con la asignación dada
    def satisfecha(self, asignacion):
        # Este método será implementado en subclases
        raise NotImplementedError


# Definición de la subclase RestriccionDistinto
class RestriccionDistinto(Restriccion):
    # Método para verificar si el valor dado es diferente a los valores asignados
    def satisfecha(self, valor, asignacion):
        # Verifica si el valor está presente en los valores asignados
        if valor in asignacion.values():
            return False
        return True


# Bloque principal del programa
if __name__ == "__main__":
    # Definición de las variables y dominios
    variables = ['A', 'B', 'C']
    dominios = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
    # Creación de la instancia del problema CSP
    csp = CSP(variables, dominios)

    # Agrega restricciones al problema CSP
    csp.agregar_restriccion(RestriccionDistinto(['A', 'B']))
    csp.agregar_restriccion(RestriccionDistinto(['B', 'C']))

    # Realiza la búsqueda por retroceso para encontrar una solución
    solucion = csp.busqueda_retroceso()
    # Imprime la solución encontrada o un mensaje indicando que no se encontró solución
    if solucion is not None:
        print("Solución encontrada:", solucion)
    else:
        print("No se encontró solución.")
