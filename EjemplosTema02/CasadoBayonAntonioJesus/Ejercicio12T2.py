# Escriba un programa que permita crear una lista de palabras y que, a continuación, ordene la lista por
# orden alfabético.

lista = []

num = int(input('Dime la cantidad de palabras que quieres añadir'))

for i in range (num):
    palabras = str(input('Introduce las palabras'))
    lista.append(palabras)

x = sorted(lista)
print(x)
