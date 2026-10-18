total = 0

precio = float(input("Ingrese el precio del producto (0 para terminar): "))

while precio != 0:
    if precio > 0:
        total = total + precio
    else:
        print("El precio no puede ser negativo")

    precio = float(input("Ingrese otro precio (0 para terminar): "))

print("Total a pagar:", total)