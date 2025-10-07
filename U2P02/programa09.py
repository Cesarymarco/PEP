"""programa09
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
• La piedra gana a la tijera pero pierde contra el papel.
• El papel gana a la piedra pero pierde contra la tijera.
• La tijera gana al papel pero pierde contra la piedra."""

import random

print("1.Piedra")
print("2.Papel")
print("3.Tijera")
opcion = int(input("Seleccione una opción (1, 2 o 3): "))
juego = random.randrange(1,4)

while opcion == juego:
    juego = random.randrange(1,4)


if(opcion == 1) and (juego == 3):
    print("GANASTE, la maquina cogio la opcion ",juego)
elif(opcion == 1) and (juego == 2):
    print("PERDISTE, la maquina cogio la opcion ",juego)
elif(opcion == 2) and (juego == 1):
    print("GANASTE, la maquina cogio la opcion ",juego)
elif(opcion == 2) and (juego == 3):
    print("PERDISTE, la maquina cogio la opcion ",juego)
elif(opcion == 3) and (juego == 2):
    print("GANASTE, la maquina cogio la opcion ",juego)
elif(opcion == 3) and (juego == 1):
    print("PERDISTE, la maquina cogio la opcion ",juego)
