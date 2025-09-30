"""programa12
Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de
millas y un número de Km, muestre respectivamente el número de millas y kilómetros. Los
resultados deben estar redondeados a 2 decimales."""
# Pedir al usuario un número de millas y un número de kilómetros
millas = float(input("Introduce el número de millas: "))
km = float(input("Introduce el número de kilómetros: "))

# Convertir millas a kilómetros y kilómetros a millas
km_desde_millas = millas * 1.61
millas_desde_km = km / 1.61

# Mostrar resultados redondeados a 2 decimales
print(f"{millas} millas equivalen a {km_desde_millas:.2f} km")
print(f"{km} km equivalen a {millas_desde_km:.2f} millas")
