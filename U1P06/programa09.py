"""programa09
Escribe un programa que calcule la calificación de estudiante en un módulo. La
calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2, 60% y RA3
20%)."""
# Pedir al usuario las calificaciones de cada RA
RA1 = float(input("Introduce la calificación de RA1 (20%): "))
RA2 = float(input("Introduce la calificación de RA2 (60%): "))
RA3 = float(input("Introduce la calificación de RA3 (20%): "))

# Calcular la calificación final
calificacion_final = RA1 * 0.2 + RA2 * 0.6 + RA3 * 0.2

# Mostrar el resultado
print("La calificación final del estudiante es:", calificacion_final)
