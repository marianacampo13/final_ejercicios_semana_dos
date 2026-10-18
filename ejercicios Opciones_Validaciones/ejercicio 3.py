intentos = 0
while intentos < 3:
    clave = input("Ingrese clave: ")
    if clave == "1234":
        print("Acceso concedido")
        break
    intentos += 1
else:
    print("Cuenta bloqueada")