##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import networkx as nx  # Importar la biblioteca NetworkX para trabajar con grafos

def graphplan(estado_inicial, estado_objetivo, acciones):
    # Crear un grafo dirigido
    G = nx.DiGraph()  # Creamos un grafo dirigido utilizando la clase DiGraph de NetworkX

    # Añadir nodos para el estado inicial y objetivo
    G.add_node('estado_inicial', tipo='estado')  # Añadimos un nodo para representar el estado inicial con un atributo 'tipo'
    G.add_node('estado_objetivo', tipo='estado')  # Añadimos un nodo para representar el estado objetivo con un atributo 'tipo'

    # Añadir nodos para las acciones
    for accion in acciones:  # Recorremos todas las acciones disponibles
        G.add_node(accion, tipo='accion')  # Añadimos un nodo para cada acción con un atributo 'tipo'

    # Añadir arcos desde el estado inicial a las acciones aplicables
    for accion in acciones:  # Recorremos todas las acciones disponibles
        if all(pre in estado_inicial for pre in acciones[accion]['precondiciones']):  # Verificamos si todas las precondiciones de la acción están en el estado inicial
            G.add_edge('estado_inicial', accion)  # Añadimos un arco desde el estado inicial hacia la acción

    # Añadir arcos desde las acciones a los estados resultantes
    for accion in acciones:  # Recorremos todas las acciones disponibles
        for efecto in acciones[accion]['efectos']:  # Recorremos todos los efectos de la acción
            G.add_edge(accion, efecto)  # Añadimos un arco desde la acción hacia el estado resultante

    # Añadir arcos desde los estados resultantes al objetivo
    for estado in estado_objetivo:  # Recorremos todos los estados objetivo
        G.add_edge(estado, 'estado_objetivo')  # Añadimos un arco desde el estado resultante hacia el estado objetivo

    # Encontrar el plan
    try:
        return nx.shortest_path(G, source='estado_inicial', target='estado_objetivo')  # Encontramos el camino más corto desde el estado inicial al estado objetivo en el grafo
    except nx.NetworkXNoPath:
        return None  # Si no se encuentra un camino, devolvemos None

# Definir el problema de planificación
estado_inicial = ['En(A)', 'Libre(A)', 'Libre(B)', 'ManoVacia']  # Definimos el estado inicial del problema
estado_objetivo = ['Sobre(A, B)', 'Libre(A)', 'ManoVacia']  # Definimos el estado objetivo del problema
acciones = {  # Definimos las acciones disponibles y sus precondiciones y efectos
    'Recoger(A)': {
        'precondiciones': ['En(A)', 'Libre(A)', 'ManoVacia'],
        'efectos': ['Sosteniendo(A)', 'Libre(A)', 'ManoVacia']
    },
    'Soltar(A)': {
        'precondiciones': ['Sosteniendo(A)'],
        'efectos': ['En(A)', 'Libre(B)', 'ManoVacia']
    },
    'Apilar(A, B)': {
        'precondiciones': ['Sosteniendo(A)', 'Libre(B)'],
        'efectos': ['Sobre(A, B)', 'Libre(A)', 'ManoVacia']
    },
    'Desapilar(A, B)': {
        'precondiciones': ['Sobre(A, B)', 'Libre(A)', 'ManoVacia'],
        'efectos': ['Sosteniendo(A)', 'Libre(B)']
    }
}

# Resolver el problema de planificación
plan = graphplan(estado_inicial, estado_objetivo, acciones)  # Resolvemos el problema de planificación utilizando el algoritmo GRAPHPLAN

# Imprimir el plan
if plan:
    print("Plan encontrado:")  # Imprimimos un mensaje indicando que se encontró un plan
    for paso in plan[1:]:  # Recorremos el plan omitiendo el primer paso (estado inicial)
        print(paso)  # Imprimimos cada paso del plan
else:
    print("No se encontró un plan.")  # Imprimimos un mensaje indicando que no se encontró un plan
