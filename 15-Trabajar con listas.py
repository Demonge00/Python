

numeros = [0, 1, 2, 5, 64, 623, 4, 56]
# Como elegir elementos de la lista
primero, segundo, *tercero = numeros
print(primero, segundo, tercero)
# Para elegir solo algunos
primero, *otros, ultimo = numeros
print(primero, otros, ultimo)


mascotas = ["Pelusa", "Caballo", "Chivito", "Lion", "Cerdito"]
# Para enumerar los elementos de la lista en forma de tuplas
for mascota in enumerate(mascotas):
    print(mascota)
    print(mascota[0])  # Devuelve la pos
    print(mascota[1])  # Devuelve el elemento
# Para separarlos por indice y elemento
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
# Para obtener el indice de un elemento primero debemos comprobar si esta
if "Chivito" in mascotas:  # Asi se comprueba
    print(mascotas.index("Chivito"))  # Este es el comando del indice
    # Retorna el numero de ocurrencias de un elemento
    print(mascotas.count("Caballo"))
# Para añadir algo a la lista
mascotas.insert(1, "Melvi")  # Añade un elemento en la posicion 1
mascotas.insert(-1, "Chancito sad")  # Añade uno al final
# Para eliminar un elemento de la lista primero hay q comprobar si esta sino da error
mascotas.remove("Dog")  # Remueve el elemento una vez
mascotas.pop()  # Remueve el ultimo elemento de un array
mascotas.pop(3)  # Remueve el elemente numero algo
del mascotas[2]  # Remueve el elemn numero algo
mascotas.clear()  # Borra todo el array
