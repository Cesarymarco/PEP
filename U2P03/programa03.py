"""programa03
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue"""

#PRIMERA FORMA FOR
print("NUMEROS PARES DEL 1 AL 10")
for i in range(1,11):
    if ( i%2 == 0):
        print(i)

#SEGUNDA FORMA FOR
print("NUMEROS PARES DEL 1 AL 10")
for i in range(1,11):
    if(i%2 != 0 ):
        continue
    print(i)

#PRIMERA FORMA WHILE
print("NUMEROS PARES DEL 1 AL 10")
x = 1
while x < 11:
    if(x%2 == 0):
        print(x)
    x+=1

#SEGUNDA FORMA WHILE
print("NUMEROS PARES DEL 1 AL 10")
n = 0
while n < 11:
    n+=1
    if(n%2 != 0):
        continue
    print(n)
    

