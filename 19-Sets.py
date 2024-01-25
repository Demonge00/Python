# Conjuto remueve los elementos duplicados
primer = {1, 2, 4, 6, 7, 8, 9, 20}  # Llaves para los sets
segundo = [3, 4, 5]
print(primer)
primer.add(5)  # Añadir a un set
primer.remove(2)  # remueve el elemnto del set
segundo = set(segundo)  # Funcion set recibe un iterable
print(segundo)
# Operadores utiles de sets
print(primer | segundo)  # Operador de union de conjuntos
print(primer & segundo)  # Operador de intereseccion de conjuntos
print(primer - segundo)  # Operador diff de conjuntos
# Operador q devuelve los elementos de ambos q no estan en la int es decir A & B Comp
print(primer ^ segundo)
if 5 in segundo:  # Para verificar si esta en el set
    print("Hello world")
