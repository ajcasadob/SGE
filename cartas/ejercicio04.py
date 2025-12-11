def palabra_mas_corta(lista_palabras):
    return min(lista_palabras, key=len)

palabras = input("Introduce palabras separadas por espacios: ").split()
print(f'La palabra mas corta de la lista es: {palabra_mas_corta(palabras)}')
