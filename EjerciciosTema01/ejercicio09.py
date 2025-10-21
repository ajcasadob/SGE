palabras = []
texto = ""

while texto.lower()!= "fin":

    texto = input("Introduce una palabra (o 'fin' para terminar): ")

    if texto.lower() != "fin": 
        palabras.append(texto)


print("\nHas introducido las siguientes palabras: ")

for palabra in palabras:
    print("-", palabras)


