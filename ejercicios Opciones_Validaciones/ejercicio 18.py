saldo = 500000

while saldo > 0:
    print("Saldo disponible:", saldo)
    retiro = int(input("Ingrese el valor a retirar (0 para salir): "))

    if retiro == 0:
        break
    elif retiro > 0 and retiro <= saldo:
        saldo = saldo - retiro
        print("Retiro realizado")
    else:
        print("Error: saldo insuficiente o valor no válido")

print("Saldo restante:", saldo)
