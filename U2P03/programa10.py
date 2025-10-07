"""programa10
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca"""

import random

banca = random.randrange(17, 22)
print("💻 La banca ya tiene su jugada (oculta).")

num_jugadores = int(input("Introduce el número de jugadores: "))

for jugador in range(1, num_jugadores + 1):
    print(f"===== Turno del Jugador {jugador} =====")
    puntuacion_jugador = 0
    
    while True:
        print(f"Tu puntuación actual: {puntuacion_jugador}")
        opcion = input("¿Quieres sacar una carta? (s/n): ").lower()
        
        if opcion != 's':
            break
        
        carta = random.randrange(1, 6)
        puntuacion_jugador += carta
        print(f"Has sacado un {carta}. Tu total ahora es {puntuacion_jugador}.")
        
        if puntuacion_jugador > 21:
            print("Te pasaste de 21. ¡Pierdes!")
            break


    print(f"Resultado final del Jugador {jugador}: {puntuacion_jugador}")
    
    if puntuacion_jugador > 21:
        print("Pierdes (te pasaste de 21).")
    elif puntuacion_jugador > banca:
        print(f"¡Ganaste! Tu puntuación ({puntuacion_jugador}) es mayor que la banca ({banca}).")
    elif puntuacion_jugador == banca:
        print(f"Empate con la banca ({banca}). La banca gana en caso de igualdad.")
    else:
        print(f"Pierdes. La banca tiene {banca}, tú {puntuacion_jugador}.")

print(f"La banca tenía: {banca}")
print("Fin de la partida.")
