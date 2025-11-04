#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y
#elimine esa palabra de la lista.

palabras = []
num = int(input('Indica el numero de palabras que quieras añadir '))
for i in range (num):
    palabra = str(input('Indique las palabras a añadir:'))
    palabras.append(palabra)

palabraEliminar = str(input('Indica la palabra que quieres eliminar:'))

if palabraEliminar not in palabras:
    print('No esta en la lista')
else:
    print(palabras)
    palabras.remove(palabraEliminar)
    print(palabras)

