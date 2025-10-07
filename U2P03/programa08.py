"""programa08
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).
Mejora el programa de forma que el usuario tenga solo 3 intentos"""

import random


print("VERSION 1")

numero_secreto = random.randrange(1, 21)

print(" Adivina el número (entre 1 y 20):")

while True:
    intento = int(input("Introduce tu número: "))
    
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print(f"¡Correcto! El número era {numero_secreto}.")
        break



print("VERSION 2")

numero_secreto2 = random.randrange(1, 21)
intentos2 = 3

print("🎯 Adivina el número (entre 1 y 20). ¡Tienes 3 intentos!")

for i in range(intentos2):
    intento2 = int(input(f"Intento {i + 1}: "))
    
    if intento2 == numero_secreto2:
        print(f" ¡Acertaste! El número era {numero_secreto2}.")
        break
    elif intento2 < numero_secreto2:
        print(" El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
else:
    print(f" Has agotado los intentos. El número era {numero_secreto2}.")

