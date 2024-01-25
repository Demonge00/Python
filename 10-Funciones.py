# Se coloca def luego nombre y parentesis y los legendarios dos pts
def Hola(nick="Joseito", apellido="jose"):
    print("Hola mundo")
    print("Ultimate Py")
    print(f"Holiwood {nick} {apellido}")
# Si se declara variable es obligatorio llamarla en los parametros y se
# separan los parametros por coma.Se puede definir un parametro por default si
# lo igualamos a algo el parametro


Hola("Alejon")  # Se llama normalmente

# Se puede nombrar un argumento de esta forma para violar el orden
Hola(apellido="Juansito")
