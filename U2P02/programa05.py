"""programa05
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
o que indique que son iguales."""

n1 = int(input("Dime un numero: "))
n2 = int(input("Dime otro numero: "))

if( n1 > n2):
    print ( "El numero ",n1," es mayor que ",n2)
elif( n1 < n2):
    print ( "El numero ",n2," es mayor que ",n1)
else:
    print ( "El numero ",n1," es igual que ",n2)