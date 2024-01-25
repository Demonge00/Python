def largo(var):
    res = 0
    for _ in var:
        res += 1
    return res


# El puntito rojo q se hace tocando la izquierda es para q el debugger comienze desde aqui
# Pues si no seleccionamos no comienza a debuguear y solo ejecuta el codigo la flechita de
# adentro es para entrar en la funcion y la de una curva para pasar a la siguiente
l = largo("afasgasgasg")
print(l)
