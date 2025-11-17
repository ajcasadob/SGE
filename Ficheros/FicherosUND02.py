#Para abrir un fichero se utiliza una funcion que se llama open ()

f = open('temps.txt','r')
print(f.read())

#Puedo evitar poner la r solo para leer
ficheroLecturaExistente = open('temps.txt')
contenidoExistente = ficheroLecturaExistente.read()
print('Contenido del fichero existente es: ')
print(contenidoExistente)

#Si queremos leer linea a linea readline () o en plural readlines ()
ficheroLecturaExistente.seek(0) ##Volvemos al inicio del fichero, por que hemos leido todo su contenido.
linea1 = ficheroLecturaExistente.readline()
print('Primera linea del fichero')
print(linea1)

#Para ir leyendo linea por linea usamos un for

print('Leyendo linea a linea con un bucle')
ficheroLecturaExistente.seek(0)

for linea in ficheroLecturaExistente:
    print(linea, end='')
    
    

#Otra forma es usar readlines () que devuelve una lista con todas las lineas

ficheroLecturaExistente.seek(0)

lineas = ficheroLecturaExistente.readlines()

print('\nEl contenido del fichero leido con realines():')
for linea in linea:
    print(linea, end='')
ficheroLecturaExistente.close()    

canary_iata = ( 'TFN' , 'TFS' , 'LPA' , 'GMZ' , 'VDE' , 'SPC' , 'ACE' , 'FUE' )
fichero_aeropuertos = open('canary_iata.txt','a')

for code in canary_iata:
    fichero_aeropuertos.write(code+'\n')
fichero_aeropuertos.close()
    

#Para escribir la tupla de una vez 

f= open('canary_iata.txt','w')
f.write('\n'.join(canary_iata))
f.close()