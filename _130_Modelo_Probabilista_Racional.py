##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class BayesianNetwork:  # Define una clase llamada BayesianNetwork
    def __init__(self):  # Define el método de inicialización de la clase
        self.nodes = {}  # Diccionario para almacenar los nodos de la red

    def add_node(self, node_name, parents, probabilities):  # Define un método para agregar un nodo a la red
        self.nodes[node_name] = {'parents': parents, 'probabilities': probabilities}  # Agrega un nodo a la red con sus padres y probabilidades

    def calculate_probability(self, node_name, evidence):  # Define un método para calcular la probabilidad de un nodo dado la evidencia
        # Verifica si el nodo está presente en la red
        if node_name not in self.nodes:
            print(f"El nodo {node_name} no está presente en la red.")
            return None

        node = self.nodes[node_name]
        parents = node['parents']
        probabilities = node['probabilities']

        # Verifica si se proporciona evidencia para todos los padres del nodo
        if set(parents) != set(evidence.keys()):
            print(f"No se proporcionó evidencia para todos los padres de {node_name}.")
            return None

        # Calcula la probabilidad condicional del nodo dados los valores de sus padres
        probability_index = tuple(evidence[parent] for parent in parents)
        probability = probabilities[probability_index]

        return probability

# Creamos una red bayesiana
bn = BayesianNetwork()

# Añadimos los nodos y sus relaciones
bn.add_node('Lluvia', [], {(): 0.2})  # Nodo raíz con probabilidad marginal de lluvia
bn.add_node('Riego', ['Lluvia'], {(True,): 0.1, (False,): 0.5})  # Nodo de riego condicionado a la lluvia

# Realizamos algunas consultas de probabilidad
print("Probabilidad de lluvia:")
print("P(Lluvia) =", bn.calculate_probability('Lluvia', {}))

print("\nProbabilidad de riego dado que está lloviendo:")
print("P(Riego | Lluvia=True) =", bn.calculate_probability('Riego', {'Lluvia': True}))

print("\nProbabilidad de riego dado que no está lloviendo:")
print("P(Riego | Lluvia=False) =", bn.calculate_probability('Riego', {'Lluvia': False}))
