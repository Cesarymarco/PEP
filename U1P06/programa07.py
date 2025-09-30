"""programa07
Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a
cuantas horas y minutos corresponde."""
# Pedir al usuario una cantidad de minutos
minutos = int(input("Introduce una cantidad de minutos: "))

# Calcular horas y minutos
horas = minutos // 60   # División entera
resto_minutos = minutos % 60  # Resto

# Mostrar resultado
print(minutos, "minutos equivalen a", horas, "hora(s) y", resto_minutos, "minuto(s).")
