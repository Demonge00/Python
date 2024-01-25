mascotas = ["Riain", "Bug", "Cat", "Wolf"]
mascotas[0] = "Lion"  # Cambia el elemmento como en js y c#
print(mascotas)
# Los indices son desde donde sale incluyendo hasta donde llega sin incluir
print(mascotas[0:2])
# Devuelve solamente el ultimo elemento y si se cambia el num sucesivamente el penultimo y asi
print(mascotas[-1])
# Toma elementos segun el salto q de en este caso es de 2 en 2 es decir uno si uno no.
# SI se pone un indice inicial parte de ahi en este caso 1
# Si se pone uno en el medio es hasta donde llegar en la iteracion ej 3 sin incluir
print(mascotas[1:4:2])
