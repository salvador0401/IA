##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class AccionCondicional:
    def __init__(self, condicion, accion):  # Define la clase AccionCondicional con un constructor que recibe una condición y una acción
        self.condicion = condicion  # Asigna la condición recibida al atributo condicion
        self.accion = accion  # Asigna la acción recibida al atributo accion

class Entorno:
    def __init__(self, estado_inicial):  # Define la clase Entorno con un constructor que recibe el estado inicial
        self.estado = estado_inicial  # Asigna el estado inicial recibido al atributo estado

    def aplicar_accion(self, accion):  # Define un método para aplicar una acción al estado del entorno
        if accion.condicion(self.estado):  # Verifica si la condición de la acción se cumple en el estado actual del entorno
            self.estado = accion.accion(self.estado)  # Aplica la acción al estado y actualiza el estado del entorno
            return True  # Retorna True si la acción se aplicó con éxito
        else:
            return False  # Retorna False si la condición de la acción no se cumple en el estado actual del entorno

# Ejemplo de uso
if __name__ == "__main__":
    # Definir las condiciones y acciones
    def condicion_soleado(estado):  # Define una función para verificar si el clima está soleado en el estado dado
        return estado['clima'] == 'soleado'

    def condicion_lluvioso(estado):  # Define una función para verificar si el clima está lluvioso en el estado dado
        return estado['clima'] == 'lluvioso'

    def accion_salir_exterior(estado):  # Define una función para ejecutar la acción de salir al exterior
        print("¡Sal al exterior!")  # Imprime un mensaje indicando salir al exterior
        return estado  # Retorna el estado sin modificar

    def accion_quedarse_adentro(estado):  # Define una función para ejecutar la acción de quedarse adentro
        print("Quédate en casa.")  # Imprime un mensaje indicando quedarse en casa
        return estado  # Retorna el estado sin modificar

    # Inicializar el entorno con un estado inicial
    estado_inicial = {'clima': 'soleado'}  # Define un estado inicial con el clima soleado
    entorno = Entorno(estado_inicial)  # Crea una instancia del entorno con el estado inicial

    # Definir acciones condicionales
    accion_si_soleado = AccionCondicional(condicion_soleado, accion_salir_exterior)  # Crea una acción condicional para salir al exterior si el clima está soleado
    accion_si_lluvioso = AccionCondicional(condicion_lluvioso, accion_quedarse_adentro)  # Crea una acción condicional para quedarse adentro si el clima está lluvioso

    # Aplicar acciones basadas en el estado actual del entorno
    entorno.aplicar_accion(accion_si_soleado)  # Aplica la acción condicional correspondiente al estado actual del entorno (clima soleado)
    entorno.aplicar_accion(accion_si_lluvioso)  # Aplica la acción condicional correspondiente al estado actual del entorno (clima soleado)
