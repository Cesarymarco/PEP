"""programa14
Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos
GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario.
La salida debe ser algo así:
1000000000 bytes en sistema decimal (SI): 1 GB, 0 MB, 0 KB, 0 bytes
1000000000 bytes en sistema binario (IEC): 0 GiB, 953 MiB, 690 KiB, 512 bytes"""
# Pedir al usuario el número de bytes
bytes_totales = int(input("Introduce el número de bytes: "))

# Sistema decimal (SI)
GB = bytes_totales // 10**9
MB = (bytes_totales % 10**9) // 10**6
KB = (bytes_totales % 10**6) // 10**3
B = bytes_totales % 10**3

print(f"{bytes_totales} bytes en sistema decimal (SI): {GB} GB, {MB} MB, {KB} KB, {B} bytes")

# Sistema binario (IEC)
GiB = bytes_totales // 2**30
MiB = (bytes_totales % 2**30) // 2**20
KiB = (bytes_totales % 2**20) // 2**10
B_bin = bytes_totales % 2**10

print(f"{bytes_totales} bytes en sistema binario (IEC): {GiB} GiB, {MiB} MiB, {KiB} KiB, {B_bin} bytes")
