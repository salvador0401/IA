##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class Persona:  # Definición de la clase Persona
    def __init__(self, nombre):  # Constructor de la clase Persona
        self.nombre = nombre  # Asignación del atributo nombre
        self.padres = []  # Inicialización de la lista de padres

    def agregar_padre(self, padre):  # Método para agregar padres
        self.padres.append(padre)  # Agregar padre a la lista de padres

    def __str__(self):  # Método especial para convertir a cadena
        return self.nombre  # Devuelve el nombre de la persona como cadena

def main():  # Función principal
    juan = Persona("Juan")  # Crear una instancia de Persona llamada Juan
    maria = Persona("Maria")  # Crear una instancia de Persona llamada Maria

    juan.agregar_padre(maria)  # Asignar a Maria como padre de Juan

    # Inferencia simple
    for persona in [juan, maria]:  # Iterar sobre las instancias de Persona
        if len(persona.padres) > 0:  # Comprobar si la persona tiene padres
            print(f"{persona} tiene padres.")  # Imprimir si tiene padres
        else:
            print(f"{persona} no tiene padres.")  # Imprimir si no tiene padres

if __name__ == "__main__":  # Entrada principal del programa
    main()  # Llamar a la función principal si se ejecuta como script

