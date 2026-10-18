
stock = 20

while stock > 0:
    print("Stock disponible:", stock)
    venta = int(input("¿Cuántas unidades desea vender? "))

    if venta > 0 and venta <= stock:
        stock = stock - venta
        print("Venta realizada")
    else:
        print("Error: cantidad no válida")

print("Inventario agotado")
