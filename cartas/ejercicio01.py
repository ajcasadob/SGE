def es_palindromo(palabra):
    return palabra == palabra[::-1]

palabra = input("Introduce una palabra: ")
if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
