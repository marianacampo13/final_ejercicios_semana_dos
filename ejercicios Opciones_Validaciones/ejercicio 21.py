presentes = 0
ausentes = 0

letra = input("Ingrese P, A o F para terminar: ").upper()

while letra != "F":
    if letra == "P":
        presentes = presentes + 1
    elif letra == "A":
        ausentes = ausentes + 1
    else:
        print("Opción no válida")

    letra = input("Ingrese P, A o F para terminar: ").upper()

print("Total de presentes:", presentes)
print("Total de ausentes:", ausentes)
