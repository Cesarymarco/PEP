"""programa04
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor."""

import math

def area_circulo(radio):
    area = math.pi * math.pow(radio,2)
    print(f"El área del circulo es de: {area} cm cuadrados")
    print(" ")

def area_triangulo(base, altura):
    area = (base*altura)/2
    print(f"El área del triangulo es de: {area} cm cuadrados")
    print(" ")

def area_rectangulo(base, altura):
    area = base*altura
    print(f"El área del rectangulo es de: {area} cm cuadrados")
    print(" ")

def mostrar_menu():
    print("1.Calcular el área de un círculo")
    print("2.Calcular el área e un triángulo")
    print("3.Calcular el área de un rectángulo")
    print("4.Salir")

def main():
    opcion = 0
    while opcion != 4:
        mostrar_menu()
        opcion = int(input("Elija un opcion de las disponibles: "))

        while(opcion < 1 or opcion > 4 ):
            opcion = int(input("Opcion incorrecta elija una disponible: "))
        
        match opcion:
            case 1: 
                opcion1()
            case 2:
                opcion2()
            case 3:
                opcion3()
            case 4:
                print("Saliendo...")

def opcion1():
    radio = float(input("Dime el radio del circulo ( debe ser mayor de 0): "))

    while radio <= 0:
        radio = float(input("He dicho que tiene que ser mayor de 0: "))
    
    area_circulo(radio)

def opcion2():
    altura = float(input("Dime la altura del triangulo: "))

    while altura <= 0:
        altura = int(input("La altura no puede ser negativa o 0, intenta de nuevo: "))

    base = float(input("Dime la base del triangulo: "))

    while base <= 0:
        base = int(input("La base no puede ser negativa o 0, intenta de nuevo: "))
    
    area_triangulo(base,altura)

def opcion3():
    base = float(input("Dime la base del rectangulo: "))

    while base <= 0:
        base = int(input("La base no puede ser negativa o 0, intenta de nuevo: "))
    
    altura = float(input("Dime la altura del rectangulo: "))

    while altura <= 0:
        altura = int(input("La altura no puede ser negativa o 0, intenta de nuevo: "))

    area_rectangulo(base,altura)


"""INICIAR PROGRAMA"""
main()