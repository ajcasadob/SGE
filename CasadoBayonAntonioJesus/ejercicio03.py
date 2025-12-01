#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre
#un mensaje cada vez que un número no sea mayor que el anterior.


def pedir_cantidad():
    cantidad = int(input("¿Cuántos números vas a introducir? "))
    return cantidad

def pedir_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        numero = int(input(f"Introduce el número {i + 1}: "))
        numeros.append(numero)
    return numeros

def comprobar_orden(numeros):
    for i in range(1, len(numeros)):
        if numeros[i] <= numeros[i - 1]:
            print(f"El número {numeros[i]} no es mayor que el anterior ({numeros[i - 1]})")

def main():
    cantidad = pedir_cantidad()
    numeros = pedir_numeros(cantidad)
    comprobar_orden(numeros)

main()

    
