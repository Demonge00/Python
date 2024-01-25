# Se usa con dos puntos y todo lo indentado dentro es lo q se itera en bulce
for num in range(5):
    print(num == 10)
print("salsa")
# For suarios en usuario se puede iterar todo aqui
for char in "Pedrito es sad":
    print(char)
numero = 1
while numero < 100:
    print(numero)
    numero *= 2
comando = ""
while comando != "salir":
    comando = input("$")
# while True:  # Bucle infinito
#     print("shit")

for i in range(4):
    for j in range(3):
        print(j, i)
