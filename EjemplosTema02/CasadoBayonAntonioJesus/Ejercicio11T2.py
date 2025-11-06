#Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes
#listas (en las que no debe haber repeticiones):


#Lista de palabras que aparecen en las dos listas.
#Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#Lista de palabras que aparecen en ambas listas



palabras = []
palabras2 = []
noRepetidos = []
noRepetidos2 = []
noRepetidos3 = []


num = int(input('Indica la cantidad de palabras: '))

for i in range (num):
    palabrasNuevas = str(input('Indica las palabras de la lista'))
    palabras.append(palabrasNuevas)

for i in range(num):
    palabrasNuevas2 = str(input('Indica las palabras de la segunda lista:'))
    palabras2.append(palabrasNuevas2)

newLista = []
for i in palabras :
    for j in palabras2:
        if i == j:
            newLista.append(i)





for i in palabras:
    if i not in palabras2:
        noRepetidos.append(i)




for i in palabras2:
    if i not in palabras:
        noRepetidos2.append(i)




for i in newLista:
    if i not in noRepetidos:
        noRepetidos3.append(i)


print(palabras)
print(palabras2)
print(newLista)
print(noRepetidos)

