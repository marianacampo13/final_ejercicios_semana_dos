suma = 0
while True:
    n = float(input("Número (0 para salir): "))
    if n == 0:
        break
    suma += n
print(f"Suma total: {suma}")