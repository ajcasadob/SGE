#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y
#sustituya la primera por la segunda en la lista.

palabras = []

num = int(input('Indica el numero de palabras que quieras añadir '))

for i in range (num):

    palabra = str(input('Indique las palabras a añadir:'))
    palabras.append(palabra)

palabraSustituir = str(input('Palabra a sustituir'))
nuevaPalabra = str(input('Indica la nueva palabra'))
for i in range (len(palabras)):
    if palabras[i]== palabraSustituir:
        palabras[i]= nuevaPalabra

print(f"Lista modificada: {palabras}")



