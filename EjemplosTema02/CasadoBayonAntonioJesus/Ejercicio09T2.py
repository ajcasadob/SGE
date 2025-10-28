#Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista
#igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta).


palabras = []

num = int(input('Indique el numero de palabras que quieres añadir a la lista: '))

for i in range (num):

    palabra = str(input('Indique las palabras {i} 1 que quieres añadir a la lista:'))
    palabras.append(palabra)

palabras_reves = []
for palabra in palabras:
    palabras_reves.insert(0, palabra)
palabras = palabras_reves

print('Lista de palabras al reves:')

print(palabras)