"""programa05
Escribe un programa que pregunte al usuario dos números y calcule su suma, resta,
multiplicación, división, módulo y potencia."""
# Pedir al usuario dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir entre 0"
modulo = num1 % num2 if num2 != 0 else "No se puede calcular el módulo con 0"
potencia = num1 ** num2

# Mostrar resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Módulo:", modulo)
print("Potencia:", potencia)
