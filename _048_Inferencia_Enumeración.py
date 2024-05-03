##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definimos la estructura de la red bayesiana
model = BayesianModel([('D', 'S')])  # D: enfermedad, S: síntoma

# Definimos las probabilidades condicionales
cpd_disease = TabularCPD('D', 2, [[0.01], [0.99]])  # P(D)
cpd_symptom = TabularCPD('S', 2, [[0.9, 0.8],  # P(S | D)
                                   [0.1, 0.2]],
                         evidence=['D'], evidence_card=[2])

# Añadimos las probabilidades condicionales al modelo
model.add_cpds(cpd_disease, cpd_symptom)

# Verificamos la validez del modelo
model.check_model()

# Creamos un objeto de inferencia para hacer consultas en la red
inference = VariableElimination(model)

# Consultamos la probabilidad de la enfermedad dado los síntomas observados
posterior = inference.query(variables=['D'], evidence={'S': 1})

# Imprimimos el resultado de la inferencia
print(posterior)
