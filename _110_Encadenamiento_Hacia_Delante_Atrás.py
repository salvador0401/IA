##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class KnowledgeBase:
    def __init__(self):
        # Inicializa la base de conocimientos con listas vacías de hechos y reglas
        self.facts = []
        self.rules = []

    def tell_fact(self, fact):
        # Agrega un hecho a la base de conocimientos
        self.facts.append(fact)

    def tell_rule(self, rule):
        # Agrega una regla a la base de conocimientos
        self.rules.append(rule)

    def forward_chain(self, query):
        # Inicializa un conjunto para almacenar hechos inferidos y una agenda para procesar
        inferred_facts = set()
        agenda = [query]

        while agenda:
            # Extrae el hecho actual de la agenda
            current_fact = agenda.pop(0)
            # Si el hecho ya está en la base de conocimientos, continúa con el siguiente hecho
            if current_fact in self.facts:
                continue

            # Agrega el hecho a los hechos inferidos
            inferred_facts.add(current_fact)

            # Itera sobre las reglas para ver si alguna puede ser aplicada
            for rule in self.rules:
                # Verifica si todos los antecedentes de la regla están en los hechos inferidos
                if all(p in inferred_facts for p in rule.antecedents):
                    # Agrega el consecuente de la regla a la agenda
                    agenda.append(rule.consequent)

        return inferred_facts

    def backward_chain(self, query):
        # Inicializa la agenda con la consulta y un camino vacío
        agenda = [(query, [])]

        while agenda:
            # Extrae el hecho actual y el camino de la agenda
            current_fact, path = agenda.pop(0)
            # Si el hecho ya está en la base de conocimientos, continúa con el siguiente hecho
            if current_fact in self.facts:
                continue

            # Actualiza el camino con el hecho actual
            path = path + [current_fact]

            # Itera sobre las reglas para ver si alguna puede ser aplicada
            for rule in self.rules:
                # Verifica si la consecuencia de la regla coincide con el hecho actual
                if rule.consequent == current_fact:
                    # Obtiene los antecedentes de la regla
                    sub_goals = rule.antecedents
                    # Crea un nuevo camino con la regla aplicada
                    new_path = path.copy()
                    new_path.append(rule)
                    # Agrega los antecedentes a la agenda con el nuevo camino
                    agenda.extend([(p, new_path) for p in sub_goals])

        return path


class Rule:
    def __init__(self, antecedents, consequent):
        # Inicializa una regla con sus antecedentes y consecuente
        self.antecedents = antecedents
        self.consequent = consequent


# Ejemplo de uso
if __name__ == "__main__":
    kb = KnowledgeBase()

    # Hechos
    kb.tell_fact("padre(juan, pepe)")
    kb.tell_fact("padre(pepe, maria)")

    # Reglas
    kb.tell_rule(Rule(["padre(X, Y)"], "abuelo(X, Z)"))

    # Consulta
    query = "abuelo(juan, maria)"

    # Encadenamiento hacia adelante
    inferred_facts = kb.forward_chain(query)
    print("Hechos inferidos con encadenamiento hacia adelante:", inferred_facts)

    # Encadenamiento hacia atrás
    path = kb.backward_chain(query)
    print("Camino encontrado con encadenamiento hacia atrás:")
    for step in path:
        if isinstance(step, Rule):
            print("Aplicar regla:", step.antecedents, "->", step.consequent)
        else:
            print("Hecho:", step)
