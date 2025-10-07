"""programa01
Escribe un programa que pida primero un número par y luego un número impar (positivos
o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
impar respectivamente), se mostrará un aviso"""

n1 = int(input("Dime un número par: "))
n2 = int(input("Dime un número impar: "))
bien = True

if((n1%2) != 0):
    bien = False
elif((n2%2) == 0):
    bien = False

if(bien):
    print("Los dos numeros son correctos.")
else:
    print("Uno de los dos números no corresponde con lo pedido.")
