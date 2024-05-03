##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de la clase Regla para representar reglas lógicas
class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente  # Guarda el antecedente de la regla
        self.consecuente = consecuente  # Guarda el consecuente de la regla

# Definición de la clase RedSemantica para representar una red semántica
class RedSemantica:
    def __init__(self):
        self.relaciones = {}  # Diccionario para almacenar relaciones en la red semántica

    def agregar_relacion(self, objeto1, relacion, objeto2):
        if objeto1 not in self.relaciones:  # Si el objeto1 no está en las relaciones, añadirlo
            self.relaciones[objeto1] = {}
        self.relaciones[objeto1][relacion] = objeto2  # Establecer la relación entre objeto1 y objeto2 bajo la clave de la relación

    def buscar_relacion(self, objeto1, relacion):
        if objeto1 in self.relaciones and relacion in self.relaciones[objeto1]:  # Si existe la relación entre objeto1 y objeto2
            return self.relaciones[objeto1][relacion]  # Retorna objeto2
        else:
            return None  # Si no se encuentra la relación, retorna None

# Crear una red semántica
red_semantica = RedSemantica()

# Agregar relaciones a la red semántica
red_semantica.agregar_relacion("gato", "es", "animal")
red_semantica.agregar_relacion("perro", "es", "animal")
red_semantica.agregar_relacion("animal", "es", "ser vivo")
red_semantica.agregar_relacion("cachorro", "es", "joven")
red_semantica.agregar_relacion("cachorro", "tiene", "patas")

# Definir reglas
reglas = [
    Regla(["gato"], ["es", "animal"]),  # Si un gato es encontrado, se infiere que es un animal
    Regla(["perro"], ["es", "animal"]),  # Si un perro es encontrado, se infiere que es un animal
    Regla(["animal"], ["es", "ser vivo"]),  # Si se encuentra un animal, se infiere que es un ser vivo
    Regla(["cachorro"], ["es", "joven"]),  # Si se encuentra un cachorro, se infiere que es joven
    Regla(["cachorro"], ["tiene", "patas"])  # Si se encuentra un cachorro, se infiere que tiene patas
]

# Consultar la red semántica y aplicar reglas
def consultar(red_semantica, reglas, objeto):
    resultado = []  # Lista para almacenar los resultados
    for regla in reglas:
        if regla.antecedente[0] == objeto:  # Si el antecedente de la regla coincide con el objeto consultado
            resultado.append((regla.consecuente[0], regla.consecuente[1]))  # Añade el consecuente a los resultados
    return resultado  # Retorna los resultados

# Consultar y mostrar resultados
objeto_consultado = "cachorro"
resultado_consulta = consultar(red_semantica, reglas, objeto_consultado)
print(f"Propiedades de '{objeto_consultado}': {resultado_consulta}")  # Imprime los resultados de la consulta
