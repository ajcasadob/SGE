numeros = []

while True:
    entrada = input("Introduce un número ( o deja en vacio para terminnar):")


    if entrada == "": 
        break

    numero = float(entrada)
    numeros.append(numero)

    print("\Has introducido los siguientes números: ")

    for numero in numeros: 
        print("-", numero)