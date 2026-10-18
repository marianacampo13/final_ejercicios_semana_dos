numero = int(input("Ingrese un número entero: "))

invertido = 0
numero = abs(numero)

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("Número invertido:", invertido)
