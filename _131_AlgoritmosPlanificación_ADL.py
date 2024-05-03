##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre  # Nombre de la acción
        self.precondiciones = precondiciones  # Condiciones que deben ser verdaderas para que la acción sea aplicable
        self.efectos = efectos  # Efectos de la acción sobre el estado

    def es_aplicable(self, estado):
        # Comprueba si todas las precondiciones de la acción son satisfechas por el estado actual
        return all(item in estado.items() for item in self.precondiciones.items())

    def aplicar(self, estado):
        if self.es_aplicable(estado):
            # Aplica los efectos de la acción al estado actual si es aplicable
            nuevo_estado = estado.copy()
            nuevo_estado.update(self.efectos)
            return nuevo_estado
        else:
            return None

class PlanificadorADL:
    def __init__(self, estado_inicial, estado_objetivo, acciones):
        self.estado_inicial = estado_inicial  # Estado inicial del problema
        self.estado_objetivo = estado_objetivo  # Estado que se quiere alcanzar (objetivo)
        self.acciones = acciones  # Lista de acciones disponibles

    def planificar(self):
        plan = []  # Lista que contendrá las acciones del plan
        estado_actual = self.estado_inicial.copy()  # Estado actual del problema

        while not self.satisface(estado_actual, self.estado_objetivo):
            # Mientras el estado actual no satisfaga el estado objetivo:
            acciones_aplicables = [accion for accion in self.acciones if accion.es_aplicable(estado_actual)]
            # Encuentra las acciones aplicables en el estado actual
            if not acciones_aplicables:
                print("No se puede alcanzar el estado objetivo desde el estado inicial.")
                return None
            accion_elegida = acciones_aplicables[0]  # Escoge la primera acción aplicable
            plan.append(accion_elegida)  # Añade la acción al plan
            estado_actual = accion_elegida.aplicar(estado_actual)  # Aplica la acción al estado actual

        return plan

    def satisface(self, estado, estado_objetivo):
        # Comprueba si el estado actual satisface el estado objetivo
        return all(item in estado.items() for item in estado_objetivo.items())

# Definir el estado inicial
estado_inicial = {"en_casa": True, "tiene_llave": False}

# Definir el estado objetivo
estado_objetivo = {"en_escuela": True, "tiene_llave": True}

# Definir las acciones disponibles
acciones = [
    Accion("ir_a_escuela", {"en_casa": True, "tiene_llave": True}, {"en_casa": False, "en_escuela": True}),
    Accion("tomar_llave", {"en_casa": True, "tiene_llave": False}, {"tiene_llave": True})
]

# Crear el planificador
planificador = PlanificadorADL(estado_inicial, estado_objetivo, acciones)

# Obtener el plan
plan = planificador.planificar()

# Imprimir el plan
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(accion.nombre)
