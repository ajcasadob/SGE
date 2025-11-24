# Realiza un programa que lea el fichero 'datos.txt' y cree un nuevo fichero 'invertido.txt' con las
#líneas en orden inverso.


archivo_entrada = open('CasadoBayonAntonioJesusFicheros/Ejercicio05/datos.txt', 'r')
lineas = archivo_entrada.readlines()
archivo_entrada.close()


lineas_invertidas = lineas[::-1]


archivo_salida = open('CasadoBayonAntonioJesusFicheros/Ejercicio05/invertido.txt', 'w')
archivo_salida.writelines(lineas_invertidas)
archivo_salida.close()


