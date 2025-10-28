#Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera
#lista los nombres de la segunda lista.

palabras1 = []
palabras2 = []
n1 = int(input("¿Cuántas palabras quieres introducir en la primera lista? "))
for i in range(n1):
    palabra = input(f"Introduce la palabra {i+1} de la primera lista: ")
    palabras1.append(palabra)

n2 = int(input("¿Cuántas palabras quieres introducir en la segunda lista? "))
for i in range(n2):
    palabra = input(f"Introduce la palabra {i+1} de la segunda lista: ")
    palabras2.append(palabra)

for palabra in palabras2:
    while palabra in palabras1:
        palabras1.remove(palabra)

print("Resultado de eliminar las palabras:")
print(palabras1)
