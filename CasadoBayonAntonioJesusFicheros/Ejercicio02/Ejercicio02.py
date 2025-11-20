#Crea un programa que añada la fecha y hora actuales al final de un fichero.
from datetime import datetime


f = open('Ejercicio02/fechas.txt','a')


fecha = datetime.now()


fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M:%S")


f.write(fecha_formateada + '\n')

f.close()

print(f"Fecha y hora añadida: {fecha_formateada}")