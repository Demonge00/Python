lista = (1, 2, 3, 4)

print(*lista)  # Separa cada uno de los elementos
# Al pasar a una funcion


def look(*lista):
    for a in lista:
        print(a)


# Para concateanr ambas listas
comb = ["casa", *lista, "asf"]
print(comb)
# Para los diccionarios seria lo mismo pero con **
punto1 = {"x": 5, "y": 20}
punto2 = {"y": 5}
# En caso q exista una pro la sobreescribe
nuevoPunto = {**punto2, **punto1, "q": 20}
print(nuevoPunto)
