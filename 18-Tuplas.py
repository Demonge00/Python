# Se usan principalmente como el const de js para no modificar
numeros = (1, 3, 4)  # Se usa con parentesis y no se puede modificar
print(numeros)
book = numeros + (3, 6, 7)  # Se pueden concat como las listas
print(book)
# FUncion tuple(recibe un iterable)
punto = tuple("agfsagas")
pasa = tuple([2, 5, 6])
