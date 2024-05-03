##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class BaseConocimiento:
    def __init__(self):
        self.hechos = set()  # Conjunto para almacenar los hechos conocidos
        self.reglas = []      # Lista para almacenar las reglas

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)  # Agrega un hecho al conjunto de hechos

    def agregar_regla(self, premisas, conclusion):
        self.reglas.append((premisas, conclusion))  # Agrega una regla a la lista de reglas

    def consultar(self, proposicion):
        return self._evaluar(proposicion)  # Consulta si una proposición es verdadera o falsa

    def _evaluar(self, proposicion):
        if proposicion in self.hechos:  # Si la proposición es un hecho conocido, devuelve Verdadero
            return True

        for premisas, conclusion in self.reglas:  # Recorre todas las reglas
            if all(p in self.hechos for p in premisas):  # Si todas las premisas de la regla son hechos conocidos
                self.hechos.add(conclusion)  # Agrega la conclusión como nuevo hecho conocido
                return conclusion == proposicion  # Devuelve Verdadero si la proposición coincide con la conclusión de la regla

        return False  # Si la proposición no se puede probar con los hechos y reglas conocidos, devuelve Falso

# Ejemplo de uso
if __name__ == "__main__":
    base_conocimiento = BaseConocimiento()
    base_conocimiento.agregar_hecho("p")  # Agrega el hecho "p" a la base de conocimiento
    base_conocimiento.agregar_hecho("q")  # Agrega el hecho "q" a la base de conocimiento
    base_conocimiento.agregar_regla(["p", "q"], "r")  # Agrega la regla: Si "p" y "q" son verdaderos, entonces "r" es verdadero
    
    print(base_conocimiento.consultar("r"))  # Consulta si la proposición "r" es verdadera en la base de conocimiento (Salida: True)
    print(base_conocimiento.consultar("p"))  # Consulta si la proposición "p" es verdadera en la base de conocimiento (Salida: True)
    print(base_conocimiento.consultar("s"))  # Consulta si la proposición "s" es verdadera en la base de conocimiento (Salida: False)
