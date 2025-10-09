"""programa05
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales)"""

import math

#VARIABLES LOCALES
def sumar():
    a = 10
    b = 15
    print(f"La suma de {a} mas {b} es {a+b}")

sumar()

#VARIABLES GLOBALES
def restar():
    print(f"La resta de {a} menos {b} es {a-b}")

a = 20
b = 10
restar()


#VARIABLES NO LOCALES
def multiplicar():

    def dividir():
        nonlocal a 
        nonlocal b 
        print(f"La division de {a} entre {b} es {a/b}")
        a = 20
        b = 4
    
    a = 50
    b = 25
    dividir()
    print(f"La multiplicacion de { a} por {b} es {a*b}")

a = 100
b = 2
multiplicar()
print(f"El numero {a} elevado a {b} es {math.pow(a,b)}")


