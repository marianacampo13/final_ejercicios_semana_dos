factorial = int(input("N para factorial: "))

while factorial < 0:
    print("Ingrese un número positivo")
    n = int(input("N para factorial: "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print(f"Factorial de {n} es {fact}")