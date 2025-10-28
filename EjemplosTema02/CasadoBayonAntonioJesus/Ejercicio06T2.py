#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y
#sustituya la primera por la segunda en la lista.

palabras = []

num = int(input('Indica el numero de palabras que quieras añadir '))

for i in range (num):

    palabra = str(input('Indique las palabras a añadir:'))
    palabras.append(palabra)



print(palabras)

palabras.reverse()

print(palabras)


