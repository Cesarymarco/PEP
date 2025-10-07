# programa08.py
# Simula un juego de dados entre dos jugadores.

import random

# Tiradas del jugador 1
dado1_j1 = random.randrange(1, 7)
dado2_j1 = random.randrange(1, 7)
total_j1 = dado1_j1 + dado2_j1

# Tiradas del jugador 2
dado1_j2 = random.randrange(1, 7)
dado2_j2 = random.randrange(1, 7)
total_j2 = dado1_j2 + dado2_j2

# Mostrar resultados
print(f"Jugador 1: {dado1_j1} y {dado2_j1} → Total = {total_j1}")
print(f"Jugador 2: {dado1_j2} y {dado2_j2} → Total = {total_j2}")

# Determinar ganador
if total_j1 > total_j2:
    print("🏆 Gana el Jugador 1 (mayor puntuación total).")
elif total_j2 > total_j1:
    print("🏆 Gana el Jugador 2 (mayor puntuación total).")
else:
    # Si hay empate en el total, se compara el valor más alto de los dados
    max_j1 = max(dado1_j1, dado2_j1)
    max_j2 = max(dado1_j2, dado2_j2)
    
    if max_j1 > max_j2:
        print("⚡ Empate en total, pero gana el Jugador 1 (mayor dado).")
    elif max_j2 > max_j1:
        print("⚡ Empate en total, pero gana el Jugador 2 (mayor dado).")
    else:
        print("🤝 Empate total (mismo total y mismos dados).")
