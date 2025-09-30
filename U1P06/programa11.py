"""programa11
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo
de viaje hasta llegar a otra ciudad B es de N segundos. Escribie un programa que
determine la hora de llegada a la ciudad B"""
# Pedir al usuario la hora de salida y el tiempo de viaje
HH = int(input("Introduce la hora de salida (HH): "))
MM = int(input("Introduce los minutos de salida (MM): "))
SS = int(input("Introduce los segundos de salida (SS): "))
N = int(input("Introduce el tiempo de viaje en segundos (N): "))

# Convertir la hora de salida a segundos
tiempo_salida_segundos = HH * 3600 + MM * 60 + SS

# Calcular el tiempo de llegada en segundos
tiempo_llegada_segundos = tiempo_salida_segundos + N

# Convertir de nuevo a HH:MM:SS
hora_llegada = (tiempo_llegada_segundos // 3600) % 24  # módulo 24 para formato de 24h
minutos_llegada = (tiempo_llegada_segundos % 3600) // 60
segundos_llegada = tiempo_llegada_segundos % 60

# Mostrar resultado
print("La hora de llegada es {:02d}:{:02d}:{:02d}".format(hora_llegada, minutos_llegada, segundos_llegada))
