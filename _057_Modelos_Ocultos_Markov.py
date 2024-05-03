##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np  # Importar la biblioteca NumPy para manipulación de matrices

class HMM:
    def __init__(self, estados, observaciones, matriz_transicion, matriz_emision, distribucion_inicial):
        # Inicializar el HMM con los parámetros dados
        self.estados = estados  # Lista de nombres de los estados del HMM
        self.observaciones = observaciones  # Lista de nombres de las observaciones del HMM
        self.matriz_transicion = matriz_transicion  # Matriz de transición entre estados
        self.matriz_emision = matriz_emision  # Matriz de emisión de observaciones por estados
        self.distribucion_inicial = distribucion_inicial  # Distribución inicial de probabilidades de los estados

    def forward(self, observacion):
        T = len(observacion)  # Longitud de la secuencia de observaciones
        N = len(self.estados)  # Número de estados en el HMM

        # Inicializar la matriz de avance (forward) alpha
        alpha = np.zeros((T, N))

        # Paso de inicialización
        alpha[0, :] = self.distribucion_inicial * self.matriz_emision[:, self.observaciones.index(observacion[0])]

        # Paso de recursión
        for t in range(1, T):
            for j in range(N):
                alpha[t, j] = np.sum(alpha[t - 1, :] * self.matriz_transicion[:, j]) * \
                              self.matriz_emision[j, self.observaciones.index(observacion[t])]

        return alpha

    def likelihood(self, observacion):
        # Calcular la probabilidad total de una secuencia de observaciones usando el algoritmo de avance
        return np.sum(self.forward(observacion)[-1, :])

# Definir los estados y las observaciones
estados = ['Soleado', 'Lluvioso']  # Dos estados posibles del tiempo
observaciones = ['Seco', 'Mojo']   # Dos observaciones posibles del tiempo

# Definir la matriz de transición
matriz_transicion = np.array([[0.7, 0.3],  # Probabilidades de transición de estado a estado
                               [0.4, 0.6]])

# Definir la matriz de emisión
matriz_emision = np.array([[0.9, 0.1],  # Probabilidades de observar cada observación en cada estado
                            [0.2, 0.8]])

# Definir la distribución inicial de probabilidades de los estados
distribucion_inicial = np.array([0.6, 0.4])  # Probabilidad inicial de estar en cada estado

# Crear el modelo HMM con los parámetros definidos
modelo_hmm = HMM(estados, observaciones, matriz_transicion, matriz_emision, distribucion_inicial)

# Calcular la probabilidad de una secuencia de observaciones dada
observacion = ['Seco', 'Mojo', 'Seco']  # Ejemplo de secuencia de observaciones
likelihood = modelo_hmm.likelihood(observacion)
print("La probabilidad de la secuencia de observaciones es:", likelihood)
