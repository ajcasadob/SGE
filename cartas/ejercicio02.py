def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    return sum(v in vocales for v in palabra)

def mas_vocales(lista_palabras):
    return max(lista_palabras, key=contar_vocales)

palabras = input("Introduce palabras separadas por espacios: ").split()
print(f'La palabra con mas vocales es: {mas_vocales(palabras)}')
