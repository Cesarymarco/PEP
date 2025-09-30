"""programa10
Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita
obtener el número invertido"""
# Pedir al usuario un número de dos cifras
numero = int(input("Introduce un número de dos cifras: "))

# Comprobar que efectivamente tenga dos cifras
if 10 <= numero <= 99:
    # Separar decenas y unidades
    decenas = numero // 10
    unidades = numero % 10

    # Invertir el número
    numero_invertido = unidades * 10 + decenas

    # Mostrar resultado
    print("El número invertido es:", numero_invertido)
else:
    print("Error: debes introducir un número de dos cifras.")
