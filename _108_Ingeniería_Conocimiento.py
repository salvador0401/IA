##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
# Base de conocimiento: Hechos y reglas
base_conocimiento = {
    "soleado": ["jugar al tenis", "ir a la playa"],  # Si está soleado, se recomienda jugar al tenis o ir a la playa
    "lluvioso": ["ver una película", "leer un libro"],  # Si está lluvioso, se recomienda ver una película o leer un libro
    "nublado": ["salir a caminar", "ir de compras"]  # Si está nublado, se recomienda salir a caminar o ir de compras
}

# Reglas para determinar qué actividad recomendar basada en el clima
def recomendar_actividad(clima):
    if clima in base_conocimiento:  # Verifica si el clima dado está en la base de conocimiento
        return base_conocimiento[clima]  # Devuelve las actividades recomendadas para ese clima
    else:
        return ["No se encontraron actividades recomendadas para este clima."]  # Si el clima no está en la base de conocimiento, devuelve un mensaje de error

# Clima actual (entrada del usuario)
clima_actual = "soleado"  # Puedes cambiar esto según el clima actual

# Obtener recomendación de actividad
recomendaciones = recomendar_actividad(clima_actual)  # Llama a la función para obtener las recomendaciones de actividad

# Imprimir recomendaciones
print("Actividades recomendadas para el clima", clima_actual + ":")  # Imprime el clima actual
for actividad in recomendaciones:  # Itera sobre cada actividad recomendada
    print("- " + actividad)  # Imprime la actividad recomendada con un guion antes
