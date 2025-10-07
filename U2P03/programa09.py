"""programa09
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana"""


import random

banca = random.randrange(17, 22)
print("💻 La banca ya tiene su jugada (oculta).")

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
        print("💥 Te pasaste de 21. ¡Pierdes!")
        break

if puntuacion_jugador <= 21:
    print(f"La banca tenía: {banca}")
    print(f"Tu puntuación final: {puntuacion_jugador}")
    
    if puntuacion_jugador > banca:
        print("¡Ganaste! Tu puntuación es mayor que la banca.")
    elif puntuacion_jugador == banca:
        print("Empate. La banca gana en caso de igualdad.")
    else:
        print("Pierdes. La banca tiene una puntuación igual o superior.")
