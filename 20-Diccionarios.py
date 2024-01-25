# Misma sintaxis q sets pero en formato de objeto de js
punto = {"x": 25, "y": 10}
print(punto)
print(punto["x"])  # La llave se pasa entre corchetes
# Para añadir un par llave valor tenemos q
punto["z"] = 24
# Para verificar q existe la llave es como en todos
if "casa" in punto:
    print(punto["casa"])
# Get sirve para llamar al valor si existe y si no existe entonces
# le asigna un valor definido por default
print(punto.get("casa", 25))
# Dos vias para eliminar llaves
del punto["x"]
del (punto["y"])
print(punto)
# Para iterar diccionarios
for valor in punto:
    print(punto[valor])
# Otra via aun mejor
for llave, valor in punto.items():
    print(valor)
