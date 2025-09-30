"""programa06
Escribe un programa que convierta un valor dado en grados Fahrenheit a grados Celsius."""
# Pedir al usuario un valor en grados Fahrenheit
fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))

# Fórmula de conversión a Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Mostrar el resultado
print("La temperatura en grados Celsius es:", celsius)
