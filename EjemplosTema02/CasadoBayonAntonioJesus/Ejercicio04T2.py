#Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un
#número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir
#la lista.


palabras = []

num=int(input('Dime cuantas palabras quieres añadir'))

for i in range (num):
    palabra = str(input('Introduce las palabras que quieres añadir'))
    palabras.append(palabra)

    
print(palabras)




