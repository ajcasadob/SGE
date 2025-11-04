# Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra.
# Ejemplos válidos de isogramas:
# background
# downstream
# six-year-old



palabra = str(input('Introduce una palabra: ')).lower()
letras_usadas = []
es_isograma = True



for letra in palabra:
    if letra in letras_usadas:
        es_isograma = False
        break
    letras_usadas.append(letra)
if es_isograma:
    print(f'La palabra "{palabra}" es un isograma.')
else:
    print(f'La palabra "{palabra}" no es un isograma.')

