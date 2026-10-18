numero1 = int(input("Ingrese el primer número positivo: "))
numero2 = int(input("Ingrese el segundo número positivo: "))

while numero2 != 0:
    residuo = numero1 % numero2
    numero1 = numero2
    numero2 = residuo

print("El MCD es:", numero1)
