"""programa02
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente."""

num = int(input("Dime un numero entre el 1 y el 10: "))

while (num < 1) or (num > 10):
    num = int(input("Incorrecto, el numero tiene que ser entre 1 y 10: "))
    