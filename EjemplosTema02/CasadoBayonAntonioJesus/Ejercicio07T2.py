#Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y
#elimine esa palabra de la lista.

palabras = []
num = int(input('Indica el numero de palabras que quieras añadir '))
for i in range (num):
    palabra = str(input('Indique las palabras a añadir:'))
    palabras.append(palabra)

print(palabras)
palabraEliminar = str(input('Indica la palabra que quieres eliminar:'))
palabras.remove(palabraEliminar)
print(palabras)

