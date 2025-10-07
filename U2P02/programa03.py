"""programa03
Escribe un programa que pida dos numero y muestre su división. Se deben tener en
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso"""
n1 = int(input("Dime un número que se va a dividir: "))
n2 = int(input("Dimne un número que va a ser el dividendo: "))

if(n2 == 0):
    print(" !!!ERROR¡¡¡ NO SE PUEDE DIVIDIR ENTRE 0")
else:
    d = n1/n2
    print("el resultado es: ", d)