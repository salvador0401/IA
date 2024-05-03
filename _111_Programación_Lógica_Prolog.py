##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
from pyDatalog import pyDatalog  # Importa la biblioteca pyDatalog

# Definimos las relaciones
pyDatalog.create_terms('padre, abuelo, X, Y, Z')  # Define los términos que se utilizarán en las relaciones y consultas

# Reglas
+padre('Juan', 'Pedro')  # Juan es padre de Pedro
+padre('Pedro', 'Pablo')  # Pedro es padre de Pablo
+padre('Pedro', 'María')  # Pedro es padre de María

abuelo(X, Y) <= padre(X, Z) & padre(Z, Y)  # Define la regla lógica para encontrar abuelos

# Consultas
print(abuelo(X, 'Pablo'))  # Imprime los abuelos de Pablo
print(abuelo(X, 'María'))  # Imprime los abuelos de María

