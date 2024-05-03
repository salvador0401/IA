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
model = BayesianModel([('D', 'S'), ('D', 'T')])  # D: enfermedad, S: síntoma, T: tratamiento

# Definimos las probabilidades condicionales
cpd_disease = TabularCPD('D', 2, [[0.01], [0.99]])  # P(D)
cpd_symptom = TabularCPD('S', 2, [[0.9, 0.8],  # P(S | D)
                                   [0.1, 0.2]],
                         evidence=['D'], evidence_card=[2])
cpd_treatment = TabularCPD('T', 2, [[0.7, 0.3],  # P(T | D)
                                    [0.3, 0.7]],
                           evidence=['D'], evidence_card=[2])

# Añadimos las probabilidades condicionales al modelo
model.add_cpds(cpd_disease, cpd_symptom, cpd_treatment)

# Verificamos la validez del modelo
model.check_model()

# Creamos un objeto de inferencia para hacer consultas en la red
inference = VariableElimination(model)

# Calculamos la probabilidad marginal de la enfermedad (D) eliminando las otras variables (S y T)
marginal_disease = inference.query(variables=['D'])

# Imprimimos el resultado de la inferencia
print(marginal_disease)
