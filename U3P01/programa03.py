"""programa03
Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
similar al siguiente:
1. Calcular el área de un círculo
2. Calcular el área de un triángulo
3. Calcular el área de un rectángulo
4. Salir
Introduce una opción (1-4):
El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la
opción 4.
Hay que diseñar y definir la siguientes funciones: :
• calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y
retorna su área.
• calcular_area_triangulo: recibe como parámetros de entrada la base y la altura
del triangulo y retorna su área.
• calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura
del rectángulo y retorna su área.
• mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.
• main(): lee por teclado la opción seleccionada por el usuario, valida que la opción
está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función
correspondiente en función de la opción seleccionada.
• opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre
sea mayor que 0 y una vez que ha validado el radio llamará a la función
calcular_area_circulo.
• opcion2: descripción: lee por teclado el valor de la base y la altura del triángulo,
valida que los dos datos son mayores que 0 y una vez que los ha validado llamará
a la función calcular_area_triangulo.
• opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que
los dos datos son mayores que 0 y una vez que los ha validado llamará a la función
calcular_area_rectangulo"""

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

    while radio == 0:
        radio = float(input("He dicho que tiene que ser mayor de 0: "))
    
    area_circulo(radio)

def opcion2():
    altura = float(input("Dime la altura del triangulo: "))
    base = float(input("Dime la base del triangulo: "))
    area_triangulo(base,altura)

def opcion3():
    base = float(input("Dime la base del rectangulo: "))
    altura = float(input("Dime la altura del rectangulo: "))
    area_rectangulo(base,altura)


"""INICIAR PROGRAMA"""
main()