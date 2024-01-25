animal = "    beast  "
print(animal.upper())  # A mayuscula
print(animal.lower())  # A minuscula
print(animal.capitalize())  # A mayuscula la primera y el resto a minuscula
print(animal.title())  # A mayuscula cada primera letra de palabras y el resto min
print(animal.strip())  # Elimina los espacios antes y despuees de el parrafo
print(animal.strip().capitalize())  # Contatenacion de metodos
print(animal.rstrip())  # Quita espacios de la derecha
print(animal.lstrip())  # Quita espacios de la izquierda
# Devuelve la posicion donde inicia el string si es -1 no esta
print(animal.find("ea"))
# Remplaza la cadena de caracterez x con y
print(animal.replace("ea", "a"))
# Ver si se encuentra una cadena en un string devuelve un bool (Si es not es lo contrario)
print("nch" in animal)
