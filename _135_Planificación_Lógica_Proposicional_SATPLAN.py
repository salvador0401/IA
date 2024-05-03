##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random  # Importa el módulo random para generar aleatoriedad

def es_estado_objetivo(estado, estado_objetivo):  # Define una función para verificar si un estado es el estado objetivo
    return all(objetivo in estado for objetivo in estado_objetivo)  # Retorna True si todos los objetivos están en el estado actual

def aplicar_accion(estado, accion):  # Define una función para aplicar una acción a un estado y obtener el nuevo estado
    nuevo_estado = estado.copy()  # Crea una copia del estado actual para modificarlo
    nuevo_estado.extend(accion['efecto'])  # Agrega los efectos de la acción al nuevo estado
    return nuevo_estado  # Retorna el nuevo estado modificado

def satplan(estado_inicial, estado_objetivo, acciones):  # Define la función principal de SATPLAN
    max_iteraciones = 1000  # Define el número máximo de iteraciones para evitar bucles infinitos
    for _ in range(max_iteraciones):  # Realiza un bucle de iteraciones máximo
        estado_actual = estado_inicial.copy()  # Inicializa el estado actual con el estado inicial
        plan = []  # Inicializa una lista para almacenar el plan de acciones

        for _ in range(len(acciones)):  # Realiza un bucle sobre todas las acciones posibles
            satisfecho = False  # Inicializa una variable para verificar si se ha encontrado un plan

            random.shuffle(acciones)  # Mezcla aleatoriamente las acciones para introducir aleatoriedad en la búsqueda

            for accion in acciones:  # Itera sobre todas las acciones posibles
                nuevo_estado = aplicar_accion(estado_actual, accion)  # Aplica la acción al estado actual para obtener un nuevo estado
                if es_estado_objetivo(nuevo_estado, estado_objetivo):  # Comprueba si el nuevo estado es el estado objetivo
                    plan.append(accion)  # Agrega la acción al plan
                    satisfecho = True  # Marca que se ha encontrado un plan
                    break  # Sale del bucle de acciones

                estado_actual = nuevo_estado  # Actualiza el estado actual con el nuevo estado generado por la acción

            if satisfecho:  # Si se ha encontrado un plan, termina la búsqueda
                break

        if satisfecho:  # Si se ha encontrado un plan, imprime el plan y termina la función
            print("Plan encontrado:")
            for accion in plan:
                print(f"Ejecutar acción {accion['nombre']}")
            return
        else:  # Si no se ha encontrado un plan después de todas las iteraciones, imprime un mensaje
            print("No se encontró un plan")
            return

# Ejemplo de uso
if __name__ == "__main__":
    estado_inicial = ['A', 'B']  # Define el estado inicial del mundo
    estado_objetivo = ['C']  # Define el estado objetivo que se desea alcanzar
    acciones = [  # Define una lista de acciones posibles, cada una con un nombre y efectos
        {'nombre': 'Accion1', 'efecto': ['B']},
        {'nombre': 'Accion2', 'efecto': ['C']}
    ]

    satplan(estado_inicial, estado_objetivo, acciones)  # Llama a la función satplan con los parámetros especificados
