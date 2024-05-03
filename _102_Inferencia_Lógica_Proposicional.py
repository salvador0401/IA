##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definimos una clase para representar fórmulas lógicas
class FormulaLogica:
    # El método __init__ inicializa la fórmula con una cadena dada
    def __init__(self, formula):
        self.formula = formula

    # El método __str__ devuelve la representación de cadena de la fórmula
    def __str__(self):
        return self.formula

    # Método para comprobar la equivalencia con otra fórmula lógica
    def equivalente(self, otra_formula):
        return self.formula == otra_formula.formula

    # Método para determinar si la fórmula es válida
    def es_valida(self):
        # Una fórmula es válida si siempre es verdadera
        # para cualquier asignación de valores a las variables
        # Por simplicidad, vamos a asumir que solo hay una variable
        return self.evaluar(True) and self.evaluar(False)

    # Método para determinar si la fórmula es satisfacible
    def es_satisfacible(self):
        # Una fórmula es satisfacible si al menos hay una asignación
        # de valores a las variables que la hace verdadera
        return self.evaluar(True) or self.evaluar(False)

    # Método para evaluar la fórmula con un valor dado para la variable
    def evaluar(self, valor):
        # Evaluamos la fórmula con el valor dado para la variable
        # Por simplicidad, vamos a asumir que solo hay una variable
        if self.formula == "¬P":
            return not valor
        elif self.formula == "P":
            return valor

# Creamos dos fórmulas para probar el programa
formula_1 = FormulaLogica("P")
formula_2 = FormulaLogica("¬P")

# Comprobamos si las fórmulas son equivalentes
print(f"Las fórmulas son equivalentes: {formula_1.equivalente(formula_2)}")

# Comprobamos si una fórmula es válida
print(f"La fórmula 1 es válida: {formula_1.es_valida()}")
print(f"La fórmula 2 es válida: {formula_2.es_valida()}")

# Comprobamos si una fórmula es satisfacible
print(f"La fórmula 1 es satisfacible: {formula_1.es_satisfacible()}")
print(f"La fórmula 2 es satisfacible: {formula_2.es_satisfacible()}")
