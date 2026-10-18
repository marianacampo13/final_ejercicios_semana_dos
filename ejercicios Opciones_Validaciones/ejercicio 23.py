import random

secreto = random.randint(1, 10)

numero = int(input("Adivina el número entre 1 y 10: "))

while numero != secreto:
    if numero > secreto:
        print("El número secreto es menor")
    else:
        print("El número secreto es mayor")

    numero = int(input("Intenta nuevamente: "))

print("¡Correcto! Adivinaste el número")
