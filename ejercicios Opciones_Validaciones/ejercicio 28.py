numero = int(input("Ingrese un número entero positivo: "))

divisores = 0
contador = 1

while contador <= numero:
    if numero % contador == 0:
        divisores = divisores + 1

    contador = contador + 1

if numero > 1 and divisores == 2:
    print("El número es primo")
else:
    print("El número no es primo")
