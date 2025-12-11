def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    return sum(letra in vocales for letra in palabra)

palabra = input("Introduce una palabra: ")
print(f'El numero total de vocales es de : {contar_vocales(palabra)}')
