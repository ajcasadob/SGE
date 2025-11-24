#Crea un programa que lea un fichero llamado 'texto.txt' y genere 'numerado.txt' con todas las líneas
#precedidas de su número.


archivo_entrada = open('CasadoBayonAntonioJesusFicheros/Ejercicio04/texto.txt', 'r')
lineas = archivo_entrada.readlines()
archivo_entrada.close()


archivo_salida = open('CasadoBayonAntonioJesusFicheros/Ejercicio04/numerado.txt', 'w')
for numero, linea in enumerate(lineas, start=1):

    archivo_salida.write(f"{numero}. {linea}")
archivo_salida.close()

print("Archivo 'numerado.txt' creado exitosamente.")

