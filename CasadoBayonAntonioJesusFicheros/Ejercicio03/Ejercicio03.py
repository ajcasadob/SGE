# Haz un programa que copie el contenido de un fichero llamado 'origen.txt' en otro llamado
#'copia.txt'.
import shutil
origen = open('CasadoBayonAntonioJesusFicheros/Ejercicio03/origen.txt','r')
copia = open('CasadoBayonAntonioJesusFicheros/Ejercicio03/copia.txt')

shutil.copy(origen,copia)

origen.