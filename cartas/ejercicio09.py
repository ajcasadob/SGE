def longitud_palabras(palabras):
    return sum(len(palabra) for palabra in palabras)

palabras = input("Introduce palabras separadas por espacios: ").split()
print(f'La cantidad total es de: {longitud_palabras(palabras)}')
