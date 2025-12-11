def numero_mayor(numeros):
    return max(numeros)

numeros = [int(n) for n in input("Introduce números separados por espacios: ").split()]
print(f'El numero mayor de la lista es : { numero_mayor(numeros)}')
