#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga
#cuántas veces aparece esa palabra en la lista.

palabras = []

num = int(input('Introduce el numero de palabras'))

for i in range (num):
    palabra = str(input('Introduce las palabras'))
    palabras.append(palabra)


numPalabra=str(input('Introduce la palabras que quieres contar'))


print(palabras.count(numPalabra))


