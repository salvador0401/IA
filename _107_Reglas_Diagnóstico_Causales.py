##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Definición de reglas de diagnóstico y causales
reglas = {
    "R1": ("síntoma1", "enfermedad1"),   # Si se presenta síntoma1, entonces es enfermedad1
    "R2": ("síntoma2", "enfermedad2"),   # Si se presenta síntoma2, entonces es enfermedad2
    "R3": ("síntoma3", "enfermedad1"),   # Si se presenta síntoma3, entonces es enfermedad1
    "R4": ("enfermedad1", "tratamiento1") # Si es enfermedad1, entonces tratamiento1
}

# Función para diagnosticar una enfermedad basada en los síntomas
def diagnosticar(sintomas):
    enfermedades = set()  # Conjunto para almacenar las enfermedades diagnosticadas

    # Iterar sobre todas las reglas
    for regla, (sintoma, enfermedad) in reglas.items():
        if sintoma in sintomas:  # Si el síntoma de la regla está presente en los síntomas dados
            enfermedades.add(enfermedad)  # Agregar la enfermedad asociada al conjunto de enfermedades diagnosticadas

    return enfermedades

# Función para encontrar el tratamiento para una enfermedad diagnosticada
def encontrar_tratamiento(enfermedad):
    for regla, (enf, trat) in reglas.items():
        if enf == enfermedad:
            return trat
    return "No se encontró tratamiento"

# Síntomas de ejemplo
sintomas_paciente = ["síntoma1", "síntoma3"]

# Diagnosticar enfermedad(es) basada en los síntomas
enfermedades_diagnosticadas = diagnosticar(sintomas_paciente)

# Imprimir diagnóstico
print("Enfermedad(es) diagnosticada(s):", enfermedades_diagnosticadas)

# Encontrar tratamiento para cada enfermedad diagnosticada
for enfermedad in enfermedades_diagnosticadas:
    tratamiento = encontrar_tratamiento(enfermedad)
    print(f"Tratamiento para {enfermedad}: {tratamiento}")
