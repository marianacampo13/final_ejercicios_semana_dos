while True:
    doc = input("Tipo documento CC, TI, CE: ").upper()
    if doc in ["CC", "TI", "CE"]:
        break
    print("Tipo no válido")