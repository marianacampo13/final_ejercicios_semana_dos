import random

dado = 0

while dado != 6:
    dado = random.randint(1, 6)
    print("Resultado del dado:", dado)

print("¡Salió un 6! Fin del juego")
