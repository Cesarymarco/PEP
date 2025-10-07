"""programa07
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no."""

print("VERSION 1")

suma = 0
contador = 0

while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"Suma total: {suma}")
    print(f"Media: {media}")
else:
    print("No se introdujeron números.")


print("VERSION 2")

suma2 = 0
contador2 = 0
numero2 = None

while numero2 != 0:
    numero2 = float(input("Introduce un número (0 para terminar): "))
    if numero2 != 0:
        suma2 += numero2
        contador2 += 1

if contador2 > 0:
    media2 = suma2 / contador2
    print(f"Suma total: {suma2}")
    print(f"Media: {media2}")
else:
    print("No se introdujeron números.")

