"""programa04
Escribe un programa que pregunte la base y altura de una rectángulo y calcule su área y
perímetro."""
# Pedir al usuario la base y la altura de un rectángulo
base = float(input("Introduce la base del rectángulo: "))
altura = float(input("Introduce la altura del rectángulo: "))

# Calcular el área y el perímetro
area = base * altura
perimetro = 2 * (base + altura)

# Mostrar resultados
print("El área del rectángulo es:", area)
print("El perímetro del rectángulo es:", perimetro)
