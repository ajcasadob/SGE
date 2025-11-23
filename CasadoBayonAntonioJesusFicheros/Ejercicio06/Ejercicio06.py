#Crea un programa que lea de un fichero y tenga las siguientes funcionalidades en un menú:
#- La palabra de mayor longitud.
#- Las veces que aparece una palabra.
#- Lea una línea aleatoria del fichero.
#- Dos funcionalidades más inventadas por tí.

import random

# Leer el archivo
archivo = open('Ejercicio06/diccionario.txt', 'r')
lineas = archivo.readlines()
archivo.close()

# Obtener todas las palabras del archivo
texto_completo = ''.join(lineas)
palabras = texto_completo.split()


while True:
    print("\n--- MENÚ ---")
    print("1. Palabra de mayor longitud")
    print("2. Contar veces que aparece una palabra")
    print("3. Leer línea aleatoria")
    print("4. Contar líneas del archivo")
    print("5. Palabra más repetida")
    print("0. Salir")
    
    opcion = input("Elige una opción: ")
    
    match opcion:
        case '1':
            palabra_larga = ""
            for palabra in palabras:
                if len(palabra) > len(palabra_larga):
                    palabra_larga = palabra
            print(f"La palabra más larga es: '{palabra_larga}' con {len(palabra_larga)} caracteres.")
        
        case '2':
            palabra_buscar = input("Introduce la palabra a buscar: ")
            contador = 0
            for palabra in palabras:
                if palabra == palabra_buscar:
                    contador = contador + 1
            print(f"La palabra '{palabra_buscar}' aparece {contador} veces.")
        
        case '3':
            numero_aleatorio = random.randint(0, len(lineas) - 1)
            print(f"Línea aleatoria: {lineas[numero_aleatorio].strip()}")
        
        case '4':
            total_lineas = 0
            for linea in lineas:
                total_lineas = total_lineas + 1
            print(f"El archivo tiene {total_lineas} líneas.")
        
        case '5':
            frecuencias = {}
            for palabra in palabras:
                if palabra in frecuencias:
                    frecuencias[palabra] = frecuencias[palabra] + 1
                else:
                    frecuencias[palabra] = 1
            palabra_max = ""
            max_veces = 0
            for palabra in frecuencias:
                if frecuencias[palabra] > max_veces:
                    max_veces = frecuencias[palabra]
                    palabra_max = palabra
            print(f"La palabra más repetida es: '{palabra_max}' con {max_veces} apariciones.")
        
        case '0':
            print("Saliendo del programa...")
            break
        
        case _:
            print("Opción no válida. Intenta de nuevo.")


