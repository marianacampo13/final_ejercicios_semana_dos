while True:
    nota = float(input("Ingrese nota 0.0 - 5.0: "))
    if 0.0 <= nota <= 5.0:
        break
    print("Nota inválida")