##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de la clase AgenteLogico
class AgenteLogico:
    # Constructor de la clase que inicializa el agente con una base de conocimiento
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento  # Inicializa la base de conocimiento del agente

    # Método para inferir la verdad de una consulta dada
    def inferir(self, consulta):
        # Aquí se implementaría el motor de inferencia lógica
        # Puede ser un algoritmo de encadenamiento hacia adelante, hacia atrás, resolución, etc.
        # Por simplicidad, este ejemplo utilizará una búsqueda en la base de conocimiento

        # Comprueba si la consulta está en la base de conocimiento
        if consulta in self.base_conocimiento:  # Si la consulta está en la base de conocimiento
            return True  # Devuelve verdadero
        else:  # Si la consulta no está en la base de conocimiento
            return False  # Devuelve falso

# Ejemplo de uso
if __name__ == "__main__":  # Comienza la ejecución del programa
    # Base de conocimiento
    base_conocimiento = {
        "Hombre(Juan)",
        "Mujer(María)",
        "Padre(Juan, Pedro)",
        "Madre(María, Pedro)",
        "Padre(Juan, Ana)",
        "Madre(María, Ana)"
    }  # Define una base de conocimiento con hechos lógicos

    # Crear un agente lógico con la base de conocimiento
    agente = AgenteLogico(base_conocimiento)  # Crea una instancia de la clase AgenteLogico

    # Consultas
    consulta1 = "Hombre(Juan)"  # Consulta sobre si Juan es un hombre
    consulta2 = "Padre(Juan, Pedro)"  # Consulta sobre si Juan es el padre de Pedro
    consulta3 = "Hombre(María)"  # Consulta sobre si María es un hombre

    # Realizar inferencias
    resultado1 = agente.inferir(consulta1)  # Realiza una inferencia sobre consulta1
    resultado2 = agente.inferir(consulta2)  # Realiza una inferencia sobre consulta2
    resultado3 = agente.inferir(consulta3)  # Realiza una inferencia sobre consulta3

    # Mostrar resultados
    print(f"¿{consulta1}? {resultado1}")  # Muestra si Juan es un hombre
    print(f"¿{consulta2}? {resultado2}")  # Muestra si Juan es el padre de Pedro
    print(f"¿{consulta3}? {resultado3}")  # Muestra si María es un hombre (falso)

