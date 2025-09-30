"""programa08
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea saber cuanto deberá pagar finalmente por su compra."""
# Pedir al usuario el total de la compra
total_compra = float(input("Introduce el total de la compra (€): "))

# Calcular descuento (15%)
descuento = total_compra * 0.15
precio_final = total_compra - descuento

# Mostrar resultados
print("Total de la compra:", total_compra, "€")
print("Descuento aplicado:", descuento, "€")
print("Precio final a pagar:", precio_final, "€")
