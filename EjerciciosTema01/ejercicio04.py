numero =  float(input("Introduce un numero:"))
numeroTwo = float(input("Introduce el segundo numero"))


if numero > numeroTwo:
    print("El numero mayor es ", numero)
elif numeroTwo > numero:
    print("El numero mayor es ", numeroTwo)
else:
    print("Los dos números son iguales")           