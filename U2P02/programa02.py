"""programa02
Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
negativo) y si el valor no es correcto, mostrará un aviso"""

n1 = int(input("Dime un número par: "))

if((n1%2) == 0):
    n2 = int(input("Dime un número impar: "))
    if((n2%2) == 0):
        print("!!!ERROR¡¡¡ EL NÚMERO NO ES IMPAR")
    else:
        print("Los dos números son correctos.")
else:
    print("!!!ERROR¡¡¡ EL NÚMERO NO ES PAR")

