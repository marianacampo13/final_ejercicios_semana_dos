deuda = float(input("Ingrese el valor de la deuda: "))
meses = int(input("Ingrese los meses de mora: "))

contador = 0

while contador < meses:
    deuda = deuda * 1.05
    contador = contador + 1

print("Saldo final adeudado:", round(deuda, 2))
