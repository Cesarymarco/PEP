"""programa04
Escribe un programa que lea por teclado un número real entre 1 y 10, simulando una
nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en
cuenta los siguientes rangos"""

n1 = int(input("Dime tu nota: "))

if(n1 < 0 ) or (n1 > 10):
    print("ERROR, NOTA NO VALIDA")
else:
    match n1:
        case 0|1|2|3|4:
            print("Su nota es INSUFICIENTE")
        case 5:
            print("Su nota es SUFICIENTE")
        case 6:
            print("Su nota es BIEN")
        case 7|8:
            print("Su nota es NOTABLE")
        case 9|10:
            print("Su nota es SOBRESALIENTE")