def suma_lista(numeros):
    return sum(numeros)

numeros = [float(n) for n in input("Introduce números separados por espacios: ").split()]
print(f'La suma total de la lista es de : {suma_lista(numeros)}')
