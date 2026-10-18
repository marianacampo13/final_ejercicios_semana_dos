clave = "1234"
while True:
    clave = input("Ingrese clave: ")
    if clave == clave:
        print("Bienvenido")
        break
    else:
        print("Clave incorrecta")