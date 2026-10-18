notas = []
while True:
    nota = float(input("Nota (-1 para terminar): "))
    if nota == -1:
        break
    notas.append(nota)
if notas:
    print(f"Promedio: {sum(notas)/len(notas)}")