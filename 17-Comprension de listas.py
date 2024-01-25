user = [["Pedro", 4], ["juan", 1], ["Leo", 5]]
nombres = []
for usuario in user:
    nombres.append(usuario[0])
print(nombres)
# Una via mas corta (map)
# Primer elemento transformacion y el segundo el bucle
n = [item[0] for item in user]
print(n)
# Una via para filtrar en una lista (filter)
n = [item for item in user if item[1] > 2]
print(n)
# Usar las funciones map y filter
# map primer arg func de extraccion y 2do arg lista a operar
p = list(map(lambda e: e[1], user))
p = list(filter(lambda e: e <= 5, p))
print(p)
