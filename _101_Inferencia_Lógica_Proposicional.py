##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Importa las funciones y clases necesarias de la biblioteca SymPy
from sympy import symbols, Not, Or, And, Implies, satisfiable

# Define una clase para la Inferencia Lógica Proposicional
class InferenciaLogicaProposicional:
    def __init__(self):
        pass

    # Método para realizar la inferencia
    def inferir(self, clausulas, consulta):
        # Agrega la negación de la consulta a las clausulas
        clausulas.append(Not(consulta))
        
        # Convierte las clausulas a una sola expresión
        expresion = And(*clausulas)
        
        # Verifica si la expresión es insatisfacible
        if satisfiable(expresion) == False:
            return "Insatisfacible"
        
        # Verifica si la consulta es satisfecha
        if satisfiable(And(*clausulas)) == True:
            return "Verdadero"
        else:
            return "Falso"

# Ejemplo de uso
if __name__ == "__main__":
    # Crea una instancia de la clase InferenciaLogicaProposicional
    inferencia = InferenciaLogicaProposicional()
    
    # Definir símbolos
    p, q, r = symbols('p q r')
    
    # Definir cláusulas (conjunto de expresiones lógicas)
    clausulas = [Or(p, q), Or(Not(p), r), Or(Not(q), Not(r))]
    
    # Consulta (una expresión lógica que se desea verificar)
    consulta = r
    
    # Realizar inferencia
    resultado = inferencia.inferir(clausulas, consulta)
    print("El resultado de la inferencia es:", resultado)
