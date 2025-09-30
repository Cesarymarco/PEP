"""programa02
Escribe un programa que
 Cree una variable que almacene el número entero 6.
 Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto
al que apunta la variable (deben ser iguales)
 Cree otra variable a la que se asigne la primera variable.
 Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto
al que apunta la variable (deben ser iguales)
 Utilice los operadores de identidad (is e is not) para comprobar y mostrar por
pantalla que los dos variables apuntan al mismo objeto y por lo tanto a la misma
posición de memoria.
 Asigne la cadena “Hola” a la primera variable.
 Muestre por pantalla el tipo del objeto que contiene la cadena “Hola” y el tipo del
objeto al que apunta la variable (deben ser iguales) (y diferentes al objeto 6).
Utilice la función isinstance() para comprobar y mostrar por pantalla que el
objeto al que apunta la primera variable es de tipo int y el de la segunda es de
tipo str."""

# Crear una variable que almacene el número entero 6
var1 = 6

# Mostrar el tipo del objeto que contiene el número 6 y el tipo al que apunta la variable
print("Valor de var1:", var1, "- Tipo del objeto:", type(6), "- Tipo de la variable:", type(var1))

# Crear otra variable a la que se asigne la primera variable
var2 = var1

# Mostrar los tipos de nuevo
print("Valor de var2:", var2, "- Tipo del objeto:", type(6), "- Tipo de la variable:", type(var2))

# Comprobar con operadores de identidad
print("¿var1 y var2 apuntan al mismo objeto?:", var1 is var2)
print("¿var1 y var2 apuntan a diferentes objetos?:", var1 is not var2)

# Asignar la cadena "Hola" a la primera variable
var1 = "Hola"

# Mostrar el nuevo tipo de var1
print("Valor de var1:", var1, "- Tipo del objeto:", type("Hola"), "- Tipo de la variable:", type(var1))

# Usar isinstance para comprobar tipos
print("¿var1 es int?:", isinstance(var1, int))
print("¿var1 es str?:", isinstance(var1, str))
print("¿var2 es int?:", isinstance(var2, int))
print("¿var2 es str?:", isinstance(var2, str))
