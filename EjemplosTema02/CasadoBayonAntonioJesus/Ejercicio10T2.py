#Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los elementos
#repetidos (dejando únicamente el primero de los elementos repetidos).


palabras =[]
num = int(input('Indique el numero de palabra que quieres añadir a la lista:'))

for i in range (num):
    palabra = str(input('Indique las palabras que quieres añadir:'))
    palabras.append(palabra)

lista_norepetidos=[]

for p  in  palabras:
    if p not in palabras:
        lista_norepetidos.append(p)


print(f'Lista original {palabras}')
print(f'Lista sin repetidos {lista_norepetidos}')



