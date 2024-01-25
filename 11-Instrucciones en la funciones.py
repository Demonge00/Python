# El asterisco funciona como el spread operator ... es decir indefinidos param
# xargs

def suma(*numbers):
    sumaa = 0
    for number in numbers:
        sumaa += number
    print(sumaa)
    return sumaa  # Retorna el resultado


# El doble asterisco es para pasar un parametro y su nombre a la funcion ej
def get_disc(**book):
    print(book["key"], book["name"])
# Es como un diccionario o algo asi


get_disc(key="key", name="pedro")
suma(1, 2, 3, 4)

# Las variables en las funciones son locales Para usarse en una funcion primero deben
# definirse dentro y no pueden usarse fuera de las funciones luego no es recomendable
# usar variables globales. Para usar una variable global aun asi se usa global nombe_de_var
