numero = int(input("Ingrese un número (0 para terminar): "))

if numero == 0:
    print("No se ingresaron números")
else:
    maximo = numero

    while numero != 0:
        if numero > maximo:
            maximo = numero

        numero = int(input("Ingrese otro número (0 para terminar): "))

    print("El número máximo es:", maximo)
