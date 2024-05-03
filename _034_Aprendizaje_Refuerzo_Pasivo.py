##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importa la librería NumPy

class AgenteAPR:
    def __init__(self, num_acciones, valor_inicial=0):
        """
        Inicializa un Agente de Aprendizaje por Refuerzo Pasivo (APR).

        Args:
            num_acciones (int): Número de acciones disponibles para el agente.
            valor_inicial (float): Valor inicial para los valores estimados de las acciones.
        """
        self.num_acciones = num_acciones  # Número de acciones disponibles para el agente
        self.valor_estimado = np.full(num_acciones, valor_inicial, dtype=float)    # Valores estimados iniciales
        self.contador_acciones = np.zeros(num_acciones)  # Contador de veces que se ha seleccionado cada acción

    def seleccionar_accion(self):
        """
        Selecciona una acción basada en los valores estimados actuales.

        Returns:
            int: Índice de la acción seleccionada.
        """
        # Selección de la acción con mayor valor estimado
        return np.argmax(self.valor_estimado)

    def actualizar_valor_estimado(self, accion, recompensa):
        """
        Actualiza el valor estimado de una acción basada en la recompensa recibida.

        Args:
            accion (int): Índice de la acción seleccionada.
            recompensa (float): Recompensa recibida por la acción seleccionada.
        """
        # Actualizar el contador de veces que se ha seleccionado la acción
        self.contador_acciones[accion] += 1
        n = self.contador_acciones[accion]  # Número de veces que se ha seleccionado la acción
        valor_antiguo = self.valor_estimado[accion]  # Valor estimado anterior de la acción
        # Actualizar el valor estimado de la acción utilizando la regla incremental
        self.valor_estimado[accion] = valor_antiguo + (1/n) * (recompensa - valor_antiguo)

def main():
    num_acciones = 5  # Número de acciones disponibles para el agente
    num_iteraciones = 1000  # Número de iteraciones o pasos de tiempo

    # Crear un agente de aprendizaje por refuerzo pasivo
    agente = AgenteAPR(num_acciones)

    for i in range(num_iteraciones):
        # El agente selecciona una acción
        accion_elegida = agente.seleccionar_accion()
        
        # Simular una recompensa para la acción seleccionada (en este ejemplo, una recompensa aleatoria)
        recompensa = np.random.normal(loc=0, scale=1)
        
        # Actualizar los valores estimados del agente basados en la recompensa recibida
        agente.actualizar_valor_estimado(accion_elegida, recompensa)

    # Imprimir los valores estimados finales del agente
    print("Valores estimados finales:")
    print(agente.valor_estimado)

if __name__ == "__main__":
    main()

