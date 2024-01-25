numeros = [23, 4, 25, 3, 6, 82, 1, 2]
listica = [[3, "asfas"], [5, "riqwr"], [4, "afsaqweras"]]
numeros.sort()  # Ordena el array xd
numeros.sort(reverse=True)  # Ordena el array de forma inversa

# Devuelve una nueva lista ya ordenada sin modificar la anterior
# Igual q la anterior se le puede pasar otro parametro reverse==true
# para q sea inverso
n = sorted(numeros)
print(numeros)
print(n)
# Ordenar listas de listas solo ordena bien si el primer elemn de cada lista es ordenable
print(sorted(listica))
# En caso de q no sea ordenable un elemento debemos definir una funcion para q devuelva el elem a ordenar
listica = [["asfas", 3], ["riqwr", 5], ["afsaqweras", 2]]


def ordena(e):  # Func q devuelve por donde se ordena
    return e[1]  # Esto es obsoleto xd


listica.sort(key=ordena)  # Se dene pasar por key el elemento
print(listica)

# Funciones lambda mucho mas practicas q es def superior
listica.sort(key=lambda e: e[1])  # Es como las funciones con flechas de js
