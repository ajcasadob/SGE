#Escribe un programa que cuente cuántas líneas NO vacías contiene un fichero 'entrada.txt' que
#tenga varias líneas de prueba.

f = open('Ejercicio01/entrada.txt','r')

lineas_no_vacias = 0
for linea in f:
    if linea.strip():  
        lineas_no_vacias += 1

f.close()

print(f"El fichero contiene {lineas_no_vacias} líneas NO vacías")