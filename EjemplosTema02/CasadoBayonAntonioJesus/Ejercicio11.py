#Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes
#listas (en las que no debe haber repeticiones):


#Lista de palabras que aparecen en las dos listas.
#Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#Lista de palabras que aparecen en ambas listas



palabras = []
palabras2 = []


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




print(palabras)
print(palabras2)
print(newLista)

